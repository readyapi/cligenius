import types
from typing_extensions import Annotated


def main(
    name: str,
    lastname: Annotated[str, types.Option(help="Last name of person to greet.")] = "",
    formal: Annotated[
        bool,
        types.Option(
            help="Say hi formally.", rich_help_panel="Customization and Utils"
        ),
    ] = False,
    debug: Annotated[
        bool,
        types.Option(
            help="Enable debugging.", rich_help_panel="Customization and Utils"
        ),
    ] = False,
):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """
    if formal:
        print(f"Good day Ms. {name} {lastname}.")
    else:
        print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    types.run(main)
