import cligenius
from typing_extensions import Annotated


def main(
    force: Annotated[bool, cligenius.Option("--force/--no-force", "-f/-F")] = False,
):
    if force:
        print("Forcing operation")
    else:
        print("Not forcing")


if __name__ == "__main__":
    cligenius.run(main)
