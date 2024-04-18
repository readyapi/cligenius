import types
from typing_extensions import Annotated


def main(config: Annotated[types.FileText, types.Option(mode="a")]):
    config.write("This is a single line\n")
    print("Config line written")


if __name__ == "__main__":
    types.run(main)
