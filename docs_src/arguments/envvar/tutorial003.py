import types


def main(name: str = types.Argument("World", envvar="AWESOME_NAME", show_envvar=False)):
    print(f"Hello Mr. {name}")


if __name__ == "__main__":
    types.run(main)
