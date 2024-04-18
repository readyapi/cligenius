import types


def main(
    name: str, lastname: str = types.Option(..., prompt="Please tell me your last name")
):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    types.run(main)
