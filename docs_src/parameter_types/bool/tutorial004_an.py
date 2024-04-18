import types
from typing_extensions import Annotated


def main(in_prod: Annotated[bool, types.Option(" /--demo", " /-d")] = True):
    if in_prod:
        print("Running in production")
    else:
        print("Running demo")


if __name__ == "__main__":
    types.run(main)
