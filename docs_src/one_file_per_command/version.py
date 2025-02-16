import cligenius

app = cligenius.Cligenius()


@app.command()
def version():
    print("My CLI Version 1.0")
