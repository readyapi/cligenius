import types


def main(user_name: str = types.Option(..., "--user-name", "-n")):
    print(f"Hello {user_name}")


if __name__ == "__main__":
    types.run(main)
