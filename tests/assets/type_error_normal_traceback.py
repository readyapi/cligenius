import types

app = types.Types()


@app.command()
def main(name: str = "morty"):
    print(name)


broken_app = types.Types()


@broken_app.command()
def broken(name: str = "morty"):
    print(name + 3)


if __name__ == "__main__":
    app(standalone_mode=False)

    types.main.get_command(broken_app)()
