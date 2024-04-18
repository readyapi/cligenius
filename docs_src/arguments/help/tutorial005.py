import types


def main(
    name: str = types.Argument(
        "Wade Wilson", help="Who to greet", show_default="Deadpoolio the amazing's name"
    ),
):
    print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
