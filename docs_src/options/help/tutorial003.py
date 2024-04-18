import types


def main(fullname: str = types.Option("Wade Wilson", show_default=False)):
    print(f"Hello {fullname}")


if __name__ == "__main__":
    types.run(main)
