import types

app = types.Types()


@app.command()
def hello(name: str = "World", formal: bool = False):
    """
    Say hi
    """
    if formal:
        types.echo(f"Good morning Ms. {name}")
    else:
        types.echo(f"Hello {name}!")


@app.command()
def bye(friend: bool = False):
    """
    Say bye
    """
    if friend:
        types.echo("Goodbye my friend")
    else:
        types.echo("Goodbye")
