from typing import Tuple

import types
from typing_extensions import Annotated


def main(
    names: Annotated[
        Tuple[str, str, str], types.Argument(help="Select 3 characters to play with")
    ] = ("Harry", "Hermione", "Ron"),
):
    for name in names:
        print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
