import cligenius
from typing_extensions import Annotated

app = cligenius.Cligenius()


@app.command()
def create(username: str):
    print(f"Creating user: {username}")


@app.command()
def delete(
    username: str,
    force: Annotated[
        bool, cligenius.Option(prompt="Are you sure you want to delete the user?")
    ],
):
    if force:
        print(f"Deleting user: {username}")
    else:
        print("Operation cancelled")


@app.command()
def delete_all(
    force: Annotated[
        bool, cligenius.Option(prompt="Are you sure you want to delete ALL users?")
    ],
):
    if force:
        print("Deleting all users")
    else:
        print("Operation cancelled")


@app.command()
def init():
    print("Initializing user database")


if __name__ == "__main__":
    app()
