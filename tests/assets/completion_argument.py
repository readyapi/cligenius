import click
import cligenius

app = cligenius.Cligenius()


def shell_complete(ctx: click.Context, param: click.Parameter, incomplete: str):
    cligenius.echo(f"ctx: {ctx.info_name}", err=True)
    cligenius.echo(f"arg is: {param.name}", err=True)
    cligenius.echo(f"incomplete is: {incomplete}", err=True)
    return ["Emma"]


@app.command(context_settings={"auto_envvar_prefix": "TEST"})
def main(name: str = cligenius.Argument(shell_complete=shell_complete)):
    """
    Say hello.
    """


if __name__ == "__main__":
    app()
