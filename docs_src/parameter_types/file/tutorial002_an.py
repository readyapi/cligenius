import types
from typing_extensions import Annotated


def main(config: Annotated[types.FileTextWrite, types.Option()]):
    config.write("Some config written by the app")
    print("Config written")


if __name__ == "__main__":
    types.run(main)
