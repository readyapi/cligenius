import cligenius


def main(name: str, lastname: str = cligenius.Option()):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    cligenius.run(main)
