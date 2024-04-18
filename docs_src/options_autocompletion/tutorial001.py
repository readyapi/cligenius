import types

app = types.Types()


@app.command()
def main(name: str = types.Option("World", help="The name to say hi to.")):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
