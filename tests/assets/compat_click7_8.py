from typing import List

import click
import types

app = types.Types()


def shell_complete(
    ctx: click.Context, param: click.Parameter, incomplete: str
) -> List[str]:
    return ["Jonny"]


@app.command(context_settings={"auto_envvar_prefix": "TEST"})
def main(
    name: str = types.Option("John", hidden=True),
    lastname: str = types.Option("Doe", "/lastname", show_default="Mr. Doe"),
    age: int = types.Option(lambda: 42, show_default=True),
    nickname: str = types.Option("", shell_complete=shell_complete),
):
    """
    Say hello.
    """
    print(f"Hello {name} {lastname}, it seems you have {age}, {nickname}")


if __name__ == "__main__":
    app()
