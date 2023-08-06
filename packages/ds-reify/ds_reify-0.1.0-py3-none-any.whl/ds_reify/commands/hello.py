from rich import print as rprint
import rich_click as rclick

from .. import CONTEXT_SETTINGS
from ..styles import DS_GREEN


@rclick.command(context_settings=CONTEXT_SETTINGS)
@rclick.option("--say", help="Who to say hello to.")
def hello(say: str) -> None:
    """Say Hello to the world"""
    rprint(
        f'[{DS_GREEN}]Hello[/]{f", [bold magenta]{say}[/]!" if say else ""}',
        ":vampire:",
    )
