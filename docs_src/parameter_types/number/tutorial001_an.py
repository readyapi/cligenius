import types
from typing_extensions import Annotated


def main(
    id: Annotated[int, types.Argument(min=0, max=1000)],
    age: Annotated[int, types.Option(min=18)] = 20,
    score: Annotated[float, types.Option(max=100)] = 0,
):
    print(f"ID is {id}")
    print(f"--age is {age}")
    print(f"--score is {score}")


if __name__ == "__main__":
    types.run(main)
