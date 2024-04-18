import types
from rich.prompt import Prompt


def main():
    name = Prompt.ask("Enter your name :sunglasses:")
    print(f"Hey there {name}!")


if __name__ == "__main__":
    types.run(main)
