import click
import types


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    click.echo("Initialized the database")


@cli.command()
def dropdb():
    click.echo("Dropped the database")


app = types.Types()


@app.command()
def sub():
    """
    A single-command Types sub app
    """
    print("Types is now below Click, the Click app is the top level")


types_click_object = types.main.get_command(app)

cli.add_command(types_click_object, "sub")

if __name__ == "__main__":
    cli()
