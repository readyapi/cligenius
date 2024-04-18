import types
from typing_extensions import Annotated


def complete_name():
    return ["Camila", "Carlos", "Sebastian"]


app = types.Types()


@app.command()
def main(
    name: Annotated[
        str, types.Option(help="The name to say hi to.", autocompletion=complete_name)
    ] = "World",
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
