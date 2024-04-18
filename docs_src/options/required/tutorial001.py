import types


def main(name: str, lastname: str = types.Option()):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    types.run(main)
