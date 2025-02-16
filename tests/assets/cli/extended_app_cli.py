import cligenius

sub_sub_app = cligenius.Cligenius()


@sub_sub_app.command()
def sub_sub_command():
    cligenius.echo("sub_sub_command")


sub_app = cligenius.Cligenius()
sub_app.add_cligenius(sub_sub_app, name="sub")


@sub_app.command()
def hello():
    cligenius.echo("hello there")


@sub_app.command()
def bye():
    cligenius.echo("bye bye")


cli = cligenius.Cligenius()
cli.add_cligenius(sub_app)


@cli.command()
def top():
    cligenius.echo("top")
