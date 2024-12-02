import cligenius
from typing_extensions import Annotated


def main(config: Annotated[cligenius.FileText, cligenius.Option()]):
    for line in config:
        print(f"Config line: {line}")


if __name__ == "__main__":
    cligenius.run(main)
