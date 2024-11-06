import cligenius

app = cligenius.Cligenius()


@app.command()
def delete():
    print("Deleting user: Hiro Hamada")


@app.command()
def create():
    print("Creating user: Hiro Hamada")


if __name__ == "__main__":
    app()
