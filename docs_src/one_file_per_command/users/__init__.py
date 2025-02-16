import cligenius

from .add import app as add_app
from .delete import app as delete_app

app = cligenius.Cligenius()

app.add_cligenius(add_app)
app.add_cligenius(delete_app)
