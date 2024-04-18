import types
from typing_extensions import Annotated


def main(
    id: Annotated[int, types.Argument(min=0, max=1000)],
    rank: Annotated[int, types.Option(max=10, clamp=True)] = 0,
    score: Annotated[float, types.Option(min=0, max=100, clamp=True)] = 0,
):
    print(f"ID is {id}")
    print(f"--rank is {rank}")
    print(f"--score is {score}")


if __name__ == "__main__":
    types.run(main)
