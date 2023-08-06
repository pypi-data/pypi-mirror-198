from functools import partial
from pathlib import Path
from typing import Optional

import jinja2
from iolanta.iolanta import Iolanta
from typer import Argument, Context, Option, Typer, echo

from iolanta_jinja2.macros import template_render
from iolanta_jinja2.process_template import process_template

cli = Typer(name='jinja2')


@cli.callback(
    invoke_without_command=True,
)
def render(
    ctx: Context,
    path: Path = Argument(
        Path('/dev/stdin'),
        exists=True,
        allow_dash=True,
        help='Template file to render, stdin by default.',
    ),
    to: Optional[Path] = Option(
        Path('/dev/stdout'),
        help='Path to write the resulting document; uses stdout by default.',
        writable=True,
    ),
):
    to.write_text(
        process_template(
            template=path.read_text(),
            iolanta=ctx.obj,
        ),
    )
