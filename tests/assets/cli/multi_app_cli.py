import types

sub_app = types.Types()


@sub_app.command()
def hello():
    types.echo("sub hello")


@sub_app.command()
def bye():
    types.echo("sub bye")


cli = types.Types()
cli.add_types(sub_app, name="sub")


@cli.command()
def top():
    types.echo("top")
