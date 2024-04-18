import types

import reigns
import towns

app = types.Types()
app.add_types(reigns.app, name="reigns")
app.add_types(towns.app, name="towns")

if __name__ == "__main__":
    app()
