import types
from typing_extensions import Annotated


def main(name: Annotated[str, types.Argument(metavar="✨username✨")] = "World"):
    print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
