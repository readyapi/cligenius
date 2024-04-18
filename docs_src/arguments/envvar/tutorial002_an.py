import types
from typing_extensions import Annotated


def main(
    name: Annotated[str, types.Argument(envvar=["AWESOME_NAME", "GOD_NAME"])] = "World",
):
    print(f"Hello Mr. {name}")


if __name__ == "__main__":
    types.run(main)
