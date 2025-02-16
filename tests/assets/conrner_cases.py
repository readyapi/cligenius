import cligenius

app = cligenius.Cligenius()


@app.command(context_settings={"auto_envvar_prefix": "TEST"})
def main(
    name: str = cligenius.Option("John", hidden=True),
    lastname: str = cligenius.Option("Doe", "/lastname", show_default="Mr. Doe"),
    age: int = cligenius.Option(lambda: 42, show_default=True),
):
    """
    Say hello.
    """
    print(f"Hello {name} {lastname}, it seems you have {age}")


if __name__ == "__main__":
    app()
