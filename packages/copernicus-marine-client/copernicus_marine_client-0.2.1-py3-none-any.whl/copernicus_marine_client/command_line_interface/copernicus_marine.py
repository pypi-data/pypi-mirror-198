import click

from copernicus_marine_client.command_line_interface.group_describe import (
    cli_group_describe,
)
from copernicus_marine_client.command_line_interface.group_subset import (
    cli_group_subset,
)

command_line_interface = click.CommandCollection(
    sources=[cli_group_describe, cli_group_subset]
)


if __name__ == "__main__":
    command_line_interface()
