import types


def complete_name():
    return ["Camila", "Carlos", "Sebastian"]


app = types.Types()


@app.command()
def main(
    name: str = types.Option(
        "World", help="The name to say hi to.", autocompletion=complete_name
    ),
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
