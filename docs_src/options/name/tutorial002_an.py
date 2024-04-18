import types
from typing_extensions import Annotated


def main(user_name: Annotated[str, types.Option("--name", "-n")]):
    print(f"Hello {user_name}")


if __name__ == "__main__":
    types.run(main)
