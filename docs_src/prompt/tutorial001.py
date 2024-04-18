import types


def main():
    person_name = types.prompt("What's your name?")
    print(f"Hello {person_name}")


if __name__ == "__main__":
    types.run(main)
