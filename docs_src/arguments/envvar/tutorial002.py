import types


def main(name: str = types.Argument("World", envvar=["AWESOME_NAME", "GOD_NAME"])):
    print(f"Hello Mr. {name}")


if __name__ == "__main__":
    types.run(main)
