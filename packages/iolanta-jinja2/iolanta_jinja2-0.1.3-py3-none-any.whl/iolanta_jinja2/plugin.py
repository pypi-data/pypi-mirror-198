from typing import Optional

from iolanta import Plugin
from typer import Typer

from iolanta_jinja2.cli import cli


class IolantaJinja2(Plugin):
    @property
    def typer_app(self) -> Optional[Typer]:
        """CLI command to render documents with Jinja2 & iolanta."""
        return cli
