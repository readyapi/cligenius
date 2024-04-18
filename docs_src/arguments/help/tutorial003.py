import types


def main(name: str = types.Argument("World", help="Who to greet")):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
