import types

import items
import lands
import users

app = types.Types()
app.add_types(users.app, name="users")
app.add_types(items.app, name="items")
app.add_types(lands.app, name="lands")

if __name__ == "__main__":
    app()
