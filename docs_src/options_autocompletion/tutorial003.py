import types

valid_names = ["Camila", "Carlos", "Sebastian"]


def complete_name(incomplete: str):
    completion = []
    for name in valid_names:
        if name.startswith(incomplete):
            completion.append(name)
    return completion


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
