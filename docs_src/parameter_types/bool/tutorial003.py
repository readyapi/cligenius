import types


def main(force: bool = types.Option(False, "--force/--no-force", "-f/-F")):
    if force:
        print("Forcing operation")
    else:
        print("Not forcing")


if __name__ == "__main__":
    types.run(main)
