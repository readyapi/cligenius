import types


def main(
    name: str, email: str = types.Option(..., prompt=True, confirmation_prompt=True)
):
    print(f"Hello {name}, your email is {email}")


if __name__ == "__main__":
    types.run(main)
