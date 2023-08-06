"""Provides PipenCliRequire"""
from __future__ import annotations

import asyncio
import importlib
import importlib.util
import http.server
import itertools
import json
import socketserver
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any, Mapping

from simpleconf import Config
from slugify import slugify
from pipen import Pipen, Proc
from pipen.utils import get_logger
from pipen.cli import CLIPlugin
from pipen_annotate import annotate

from .defaults import (
    PIPEN_CLI_CONFIG_DIR,
    PIPELINE_OPTIONS,
    SECTION_PIPELINE_OPTIONS,
    SECTION_PROCGROUPS,
    SECTION_PROCESSES,
)
from .version import __version__

if TYPE_CHECKING:  # pragma: no cover
    from argx import ArgumentParser, Namespace

logger = get_logger("config", "info")


def _anno_to_argspec(anno: Mapping[str, Any] | None) -> Mapping[str, Any]:
    """Convert the annotation to the argument spec"""
    if anno is None:
        return {}

    argspec = {}
    # arginfo: attrs, help, terms
    for arg, arginfo in anno.items():
        argspec[arg] = arginfo.attrs.copy()
        if (
            argspec[arg].get("type") in ("ns", "namespace")
            or argspec[arg].get("action") in ("ns", "namespace")
            or argspec[arg].get("ns") is True
            or argspec[arg].get("namespace") is True
        ):
            argspec[arg]["type"] = "ns"
            argspec[arg]["value"] = _anno_to_argspec(arginfo.terms)
        elif (
            argspec[arg].get("type") in ("choice", "choices")
            or argspec[arg].get("action") in ("choice", "choices")
            or argspec[arg].get("choice") is True
            or argspec[arg].get("choices") is True
        ):
            argspec[arg]["type"] = "choice"
            argspec[arg]["value"] = argspec[arg].pop("default", [])
            argspec[arg]["choices"] = list(arginfo.terms)
            argspec[arg]["choices_desc"] = [
                term.help for term in arginfo.terms.values()
            ]
        elif (
            argspec[arg].get("type") in ("mchoice", "mchoices")
            or argspec[arg].get("action") in ("mchoice", "mchoices")
            or argspec[arg].get("mchoice") is True
            or argspec[arg].get("mchoices") is True
        ):
            argspec[arg]["type"] = "mchoice"
            argspec[arg]["value"] = argspec[arg].pop("default", [])
            argspec[arg]["choices"] = list(arginfo.terms)
            argspec[arg]["choices_desc"] = [
                term.help for term in arginfo.terms.values()
            ]
        else:
            argspec[arg]["value"] = argspec[arg].pop("default", None)
        argspec[arg]["desc"] = arginfo.help

    return argspec


def _proc_to_argspec(anno: Proc) -> Mapping[str, Any]:
    """Convert the proc to the argument spec"""
    summary = anno.get("Summary", {"short": "", "long": ""})
    argspec = {
        "desc": f'# {summary["short"]}\n\n{summary["long"]}',
        "value": {},
    }
    argspec["value"]["envs"] = {
        "desc": f"Environment variables for the process, used across jobs",
        "value": _anno_to_argspec(anno.get("Envs", {})),
    }
    argspec["value"]["plugin_opts"] = PIPELINE_OPTIONS["plugin_opts"]
    argspec["value"]["scheduler_opts"] = PIPELINE_OPTIONS["scheduler_opts"]
    argspec["value"]["forks"] = PIPELINE_OPTIONS["forks"]
    argspec["value"]["cache"] = PIPELINE_OPTIONS["cache"]
    argspec["value"]["scheduler"] = PIPELINE_OPTIONS["scheduler"]
    argspec["value"]["dirsig"] = PIPELINE_OPTIONS["dirsig"]
    argspec["value"]["error_strategy"] = PIPELINE_OPTIONS["error_strategy"]
    argspec["value"]["num_retries"] = PIPELINE_OPTIONS["num_retries"]

    return argspec


class PipenCliConfigPlugin(CLIPlugin):
    """Check the requirements of a pipeline"""

    version = __version__
    name = "config"

    def __init__(
        self,
        parser: ArgumentParser,
        subparser: ArgumentParser,
    ) -> None:
        super().__init__(parser, subparser)
        subparser.add_argument(
            "--c-port",
            type=int,
            default=18521,
            dest="c_port",
            help="Port to serve the UI wizard",
        )
        subparser.add_argument(
            "--c-additional",
            dest="c_additional",
            help=(
                "Additional arguments for the pipeline, "
                "in YAML, INI, JSON or TOML format"
            ),
        )
        subparser.add_argument(
            "--c-force",
            action="store_true",
            dest="c_force",
            help=(
                "Force re-generating the pipeline data. "
                "Note that previously saved data will be lost."
            ),
        )
        subparser.add_argument(
            "--c-noserve",
            action="store_true",
            dest="c_noserve",
            help=(
                "Do not serve the UI wizard, "
                "just generate the pipeline data file instead.\n"
                "Implies --c-force."
            ),
            default=False,
        )
        subparser.add_argument(
            "pipeline",
            help=(
                "The pipeline and the CLI arguments to run the pipeline. "
                "For the pipeline either `/path/to/pipeline.py:<pipeline>` "
                "or `<module.submodule>:<pipeline>` "
                "`<pipeline>` must be an instance of `Pipen` and running "
                "the pipeline should be called under `__name__ == '__main__'."
            ),
        )

    def parse_args(self) -> Namespace:
        parsed, rest = self.parser.parse_known_args(fromfile_keep=True)
        parsed.pipeline_args = rest
        return parsed

    def _parse_pipeline(self, pipeline: str) -> Pipen:
        """Parse the pipeline"""
        modpath, sep, name = pipeline.rpartition(":")
        if sep != ":":
            raise ValueError(
                f"Invalid pipeline: {pipeline}.\n"
                "It must be in the format '<module[.submodule]>:pipeline' or \n"
                "'/path/to/pipeline.py:pipeline'"
            )

        path = Path(modpath)
        if path.is_file():
            spec = importlib.util.spec_from_file_location(path.stem, modpath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        else:
            module = importlib.import_module(modpath)

        try:
            pipeline = getattr(module, name)
        except AttributeError:
            raise ValueError(f"Invalid pipeline: {pipeline}") from None

        if isinstance(pipeline, type) and issubclass(pipeline, Pipen):
            pipeline = pipeline()

        if not isinstance(pipeline, Pipen):
            raise ValueError(
                f"Invalid pipeline: {pipeline}\n"
                "It must be a `pipen.Pipen` instance"
            )

        return pipeline

    async def _get_pipeline_data(self, args: Namespace) -> Mapping[str, Any]:
        """Get the pipeline data"""
        cached_file = PIPEN_CLI_CONFIG_DIR / f"{slugify(args.pipeline)}.json"
        if not args.c_force and cached_file.exists():
            logger.warning(f"Loading pipeline data from {cached_file}")
            logger.warning(
                "Remove the file to force re-generating the pipeline data"
            )
            logger.warning(
                "Or use `--c-force` to force re-generating the pipeline data"
            )
            with cached_file.open() as f:
                return json.load(f)

        if args.c_force:
            logger.warning("You are forcing re-generating the pipeline data.")
            logger.warning("Previously saved data will be loaded.")

        if cached_file.exists():
            cached_file.rename(cached_file.with_suffix(".json.bak"))
            logger.warning(
                "Moved previously saved data to "
                f"{cached_file.with_suffix('.json.bak')}"
            )

        old_argv = sys.argv
        sys.argv = ["from-pipen-cli-config"] + args.pipeline_args
        logger.info("Fetching pipeline data ...")
        try:
            pipeline = self._parse_pipeline(args.pipeline)
            # Initialize the pipeline so that the arguments definied by
            # other plugins (i.e. pipen-args) to take in place.
            await pipeline._init()
            pipeline.build_proc_relationships()
        finally:
            sys.argv = old_argv

        if args.c_additional:
            data = Config.load(args.c_additional)
        else:
            data = {}

        data[SECTION_PIPELINE_OPTIONS] = PIPELINE_OPTIONS
        data[SECTION_PIPELINE_OPTIONS]["name"] = {
            "type": "str",
            "value": pipeline.name,
            "placeholder": pipeline.name,
            # used for saving
            "cached_file": cached_file.name,
            "desc": (
                "The name of the pipeline. "
                "It will affect the names of working directory and "
                "the result directory"
            ),
        }
        data[SECTION_PIPELINE_OPTIONS]["desc"] = {
            "type": "str",
            "value": pipeline.desc,
            "desc": (
                "The description of the pipeline, "
                "shows in the log and report."
            ),
        }
        data[SECTION_PIPELINE_OPTIONS]["outdir"] = {
            "desc": "The output directory of your pipeline",
            "placeholder": "./<name>_results",
            "type": "str",
            "value": "",
        }
        data[SECTION_PROCESSES] = {}
        data[SECTION_PROCGROUPS] = {}
        for proc in pipeline.procs:
            if isinstance(proc, Proc):
                annotated = annotate(proc.__class__)
            else:
                annotated = annotate(proc)

            if proc.__procgroup__:
                if proc.__procgroup__.name not in data[SECTION_PROCGROUPS]:
                    data[SECTION_PROCGROUPS][proc.__procgroup__.name] = {
                        "PROCESSES": {}
                    }
                    pg_args = _anno_to_argspec(
                        annotate(proc.__procgroup__.__class__).get(
                            "Args", None
                        )
                    )
                    if pg_args:
                        data[SECTION_PROCGROUPS][proc.__procgroup__.name][
                            "ARGUMENTS"
                        ] = pg_args

                data[SECTION_PROCGROUPS][proc.__procgroup__.name][
                    SECTION_PROCESSES
                ][proc.name] = _proc_to_argspec(annotated)
            else:
                data[SECTION_PROCESSES][proc.name] = _proc_to_argspec(annotated)

        cached_file.parent.mkdir(parents=True, exist_ok=True)
        with cached_file.open("w") as f:
            json.dump(data, f, indent=2)

        return data

    def exec_command(self, args: Namespace) -> None:
        """Execute the command"""
        logger.info(
            "[bold]pipen-cli-config: [/bold]"
            "UI wizard to generate configuration for pipen pipelines"
        )
        logger.info(f"[bold]version: [/bold]{__version__}")
        logger.info("")

        if args.c_noserve:
            logger.info("Not serving the UI")
            args.c_force = True
            data = asyncio.run(self._get_pipeline_data(args))
            cached_file = PIPEN_CLI_CONFIG_DIR.joinpath(
                data["PIPELINE_OPTIONS"]["name"]["cached_file"]
            )
            logger.info(f"Pipeline data saved to {cached_file}")
            return

        # Avoid data to be loaded twice in do_GET in the same session
        loaded_data = None

        class HTTPHandler(http.server.SimpleHTTPRequestHandler):
            # python 3.9 doesn't have this
            _control_char_table = str.maketrans(
                {
                    c: fr'\x{c:02x}'
                    for c in itertools.chain(range(0x20), range(0x7f,0xa0))
                }
            )
            _control_char_table[ord('\\')] = r'\\'

            def __init__(this, *args, **kwargs):
                path = Path(__file__).parent / "frontend"
                super().__init__(*args, directory=path, **kwargs)

            def do_GET(this):
                if this.path == "/schema/pipeline.json":
                    nonlocal loaded_data
                    if loaded_data is None:
                        loaded_data = json.dumps(
                            asyncio.run(self._get_pipeline_data(args))
                        ).encode("utf-8")
                    this.send_response(200)
                    this.send_header("Content-type", "application/json")
                    this.end_headers()
                    this.wfile.write(loaded_data)
                else:
                    try:
                        super().do_GET()
                    except BrokenPipeError:
                        pass

            def do_POST(this):
                if this.path == "/save":
                    if not loaded_data:
                        logger.warning(
                            "Skipping saving pipeline data, "
                            "since it's not loaded yet. "
                            "Please reload the page and try again."
                        )
                        return

                    this.send_response(200)
                    this.send_header("Content-type", "application/json")
                    this.end_headers()
                    data = json.loads(
                        this.rfile.read(
                            int(this.headers["Content-Length"])
                        ).decode("utf-8")
                    )
                    cached_file = PIPEN_CLI_CONFIG_DIR.joinpath(
                       data["PIPELINE_OPTIONS"]["name"]["cached_file"]
                    )
                    with cached_file.open("w") as f:
                        json.dump(data, f, indent=2)
                    logger.info("Saved pipeline data to %s", cached_file)
                else:
                    super().do_POST()

            def log_message(this, format: str, *args: Any) -> None:
                message = format % args
                message = (
                    f"[{this.address_string()}] "
                    f"{message.translate(this._control_char_table)}"
                )
                logger.info(message)

        port = getattr(args, "c-port", 0)

        socketserver.TCPServer.allow_reuse_address = True
        with socketserver.TCPServer(("", args.c_port), HTTPHandler) as httpd:
            port = httpd.server_address[1]
            logger.info(f"Serving UI wizard at http://localhost:{port}")
            logger.info("Press Ctrl+C to exit")
            logger.info("")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                logger.error("Stopping the server")
