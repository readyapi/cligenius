import types
from typing_extensions import Annotated


def main(
    name: Annotated[str, types.Option("--name", "-n")],
    formal: Annotated[bool, types.Option("--formal", "-f")] = False,
):
    if formal:
        print(f"Good day Ms. {name}.")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
