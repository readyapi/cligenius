import types
from typing_extensions import Annotated

app = types.Types()


@app.command()
def main(name: str, email: Annotated[str, types.Option(prompt=True)]):
    print(f"Hello {name}, your email is: {email}")


if __name__ == "__main__":
    app()
