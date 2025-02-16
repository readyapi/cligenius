import cligenius

app = cligenius.Cligenius()


@app.command()
def delete(name: str):
    print(f"Deleting user: {name}")
