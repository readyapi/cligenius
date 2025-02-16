import cligenius

cli = cligenius.Cligenius()
sub_app = cligenius.Cligenius()
cli.add_cligenius(sub_app)


@sub_app.command()
def hello():
    cligenius.echo("hello there")


@sub_app.command()
def bye():
    cligenius.echo("bye bye")
