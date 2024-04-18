import types

application = types.Types()


@application.command()
def callback(name: str = "World"):
    types.echo(f"Hello {name}")
