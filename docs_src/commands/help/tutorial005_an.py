import types
from typing_extensions import Annotated

app = types.Types(rich_markup_mode="markdown")


@app.command()
def create(
    username: Annotated[str, types.Argument(help="The username to be **created**")],
):
    """
    **Create** a new *shinny* user. :sparkles:

    * Create a username

    * Show that the username is created

    ---

    Learn more at the [Types docs website](https://types.khulnasoft.com)
    """
    print(f"Creating user: {username}")


@app.command(help="**Delete** a user with *USERNAME*.")
def delete(
    username: Annotated[str, types.Argument(help="The username to be **deleted**")],
    force: Annotated[bool, types.Option(help="Force the **deletion** :boom:")] = False,
):
    """
    Some internal utility function to delete.
    """
    print(f"Deleting user: {username}")


if __name__ == "__main__":
    app()
