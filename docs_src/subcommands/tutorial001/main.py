import types

import items
import users

app = types.Types()
app.add_types(users.app, name="users")
app.add_types(items.app, name="items")

if __name__ == "__main__":
    app()
