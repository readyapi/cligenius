import types
from typing_extensions import Annotated


def main(config: Annotated[types.FileText, types.Option()]):
    for line in config:
        print(f"Config line: {line}")


if __name__ == "__main__":
    types.run(main)
