import types
from typing_extensions import Annotated


def main(force: Annotated[bool, types.Option("--force/--no-force", "-f/-F")] = False):
    if force:
        print("Forcing operation")
    else:
        print("Not forcing")


if __name__ == "__main__":
    types.run(main)
