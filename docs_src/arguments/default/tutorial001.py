import types


def main(name: str = types.Argument("Wade Wilson")):
    print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
