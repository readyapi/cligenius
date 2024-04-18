import types
from typing_extensions import Annotated


def main(name: Annotated[str, types.Argument()] = "Wade Wilson"):
    print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
