import types


def main(
    name: str = types.Option(..., "--name", "-n"),
    formal: bool = types.Option(False, "--formal", "-f"),
):
    if formal:
        print(f"Good day Ms. {name}.")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
