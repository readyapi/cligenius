import types


def main(
    id: int = types.Argument(..., min=0, max=1000),
    age: int = types.Option(20, min=18),
    score: float = types.Option(0, max=100),
):
    print(f"ID is {id}")
    print(f"--age is {age}")
    print(f"--score is {score}")


if __name__ == "__main__":
    types.run(main)
