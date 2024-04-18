import types


def main(user_name: str = types.Option(..., "--name")):
    print(f"Hello {user_name}")


if __name__ == "__main__":
    types.run(main)
