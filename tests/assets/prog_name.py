import cligenius

app = cligenius.Cligenius()


@app.command()
def main(i: int):  # pragma: no cover
    pass


if __name__ == "__main__":
    app(prog_name="custom-name")
