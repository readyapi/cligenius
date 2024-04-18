from typing import Optional

import types
from typing_extensions import Annotated


def main(name: Annotated[Optional[str], types.Argument()] = None):
    if name is None:
        print("Hello World!")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
