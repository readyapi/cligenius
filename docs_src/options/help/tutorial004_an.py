import types
from typing_extensions import Annotated


def main(
    fullname: Annotated[
        str, types.Option(show_default="Deadpoolio the amazing's name")
    ] = "Wade Wilson",
):
    print(f"Hello {fullname}")


if __name__ == "__main__":
    types.run(main)
