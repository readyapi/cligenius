import types
from typing_extensions import Annotated


def main(name: str, lastname: Annotated[str, types.Option(prompt=True)]):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    types.run(main)
