import cligenius

from .users import app as users_app
from .version import app as version_app

app = cligenius.Cligenius()

app.add_cligenius(version_app)
app.add_cligenius(users_app, name="users")


if __name__ == "__main__":
    app()
