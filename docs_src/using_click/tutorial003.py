import click
import types

app = types.Types()


@app.command()
def top():
    """
    Top level command, form Types
    """
    print("The Types app is at the top level")


@app.callback()
def callback():
    """
    Types app, including Click subapp
    """


@click.command()
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo("Hello %s!" % name)


types_click_object = types.main.get_command(app)

types_click_object.add_command(hello, "hello")

if __name__ == "__main__":
    types_click_object()
