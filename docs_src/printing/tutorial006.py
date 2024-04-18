import types


def main(name: str):
    types.secho(f"Welcome here {name}", fg=types.colors.MAGENTA)


if __name__ == "__main__":
    types.run(main)
