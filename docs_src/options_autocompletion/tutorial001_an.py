import types
from typing_extensions import Annotated

app = types.Types()


@app.command()
def main(name: Annotated[str, types.Option(help="The name to say hi to.")] = "World"):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
