import cligenius

app = cligenius.Cligenius()


@app.command()
def add(name: str):
    print(f"Adding user: {name}")
