from os import getenv

import rich_click as rclick

# builtin colors: https://rich.readthedocs.io/en/latest/appendix/colors.html
# styling: https://rich.readthedocs.io/en/latest/style.html#styles

RICH_GREEN = "dark_sea_green4"  # #5faf5f
DS_GREEN = "#62A660"

RICH_PURPLE = "medium_purple4"  # #5F5F87
DS_PURPLE_LIGHT = "#59559E"
DS_PURPLE_DARK = "#464272"

# configuration options: https://github.com/ewels/rich-click#configuration-options

rclick.rich_click.USE_RICH_MARKUP = True

# 'Usage:' text
rclick.rich_click.STYLE_USAGE = "italic"
# text after 'Usage', ie 'dsreify [] ...'
rclick.rich_click.STYLE_USAGE_COMMAND = f"bold {DS_PURPLE_LIGHT}"
# text of 'OPTIONS', 'COMMAND', and 'ARGS' in usage string
rclick.rich_click.STYLE_ARGUMENT = f"bold {RICH_GREEN}"
# help text for main, first line
rclick.rich_click.STYLE_HELPTEXT_FIRST_LINE = ""
# help text for main, rest of lines
rclick.rich_click.STYLE_HELPTEXT = "dim"
# Options long flags, eg '--help'
rclick.rich_click.STYLE_OPTION = f"bold {DS_GREEN}"
# Options short flags, eg '-h'
rclick.rich_click.STYLE_SWITCH = f"bold {DS_GREEN}"
# Option type, eg '<TEXT INTEGER FLOAT '
rclick.rich_click.STYLE_METAVAR = f"bold italic {DS_GREEN}"
# Option default value eg '[default: ]', when show_default=True
rclick.rich_click.STYLE_OPTION_DEFAULT = "dim"
# help text for options and commands
rclick.rich_click.STYLE_OPTION_HELP = ""
# style of Options help text, alternates array elements row by row
rclick.rich_click.STYLE_OPTIONS_TABLE_ROW_STYLES = [""]
# style of the Commands, alternates array elements row by row
rclick.rich_click.STYLE_COMMANDS_TABLE_ROW_STYLES = [""]
# with of the terminal, None for auto size
rclick.rich_click.MAX_WIDTH = (
    int(getenv("TERMINAL_WIDTH")) if getenv("TERMINAL_WIDTH") else 80  # type: ignore
)
# show positional arguments
rclick.rich_click.SHOW_ARGUMENTS = True
# don't group them with the Options
rclick.rich_click.GROUP_ARGUMENTS_OPTIONS = False
