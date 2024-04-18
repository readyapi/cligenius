import types


def main(
    name: str = types.Argument(..., help="Who to greet"),
    lastname: str = types.Argument(
        "", help="The last name", rich_help_panel="Secondary Arguments"
    ),
    age: str = types.Argument(
        "", help="The user's age", rich_help_panel="Secondary Arguments"
    ),
):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)
