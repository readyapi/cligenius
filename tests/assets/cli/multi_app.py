import types

sub_app = types.Types()

variable = "Some text"


@sub_app.command()
def hello(name: str = "World", age: int = types.Option(0, help="The age of the user")):
    """
    Say Hello
    """
    types.echo(f"Hello {name}")


@sub_app.command()
def hi(user: str = types.Argument("World", help="The name of the user to greet")):
    """
    Say Hi
    """


@sub_app.command()
def bye():
    """
    Say bye
    """
    types.echo("sub bye")


app = types.Types(help="Demo App", epilog="The end")
app.add_types(sub_app, name="sub")


@app.command()
def top():
    """
    Top command
    """
    types.echo("top")
