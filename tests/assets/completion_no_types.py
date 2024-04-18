import types

app = types.Types()


def complete(ctx, args, incomplete):
    types.echo(f"info name is: {ctx.info_name}", err=True)
    types.echo(f"args is: {args}", err=True)
    types.echo(f"incomplete is: {incomplete}", err=True)
    return [
        ("Camila", "The reader of books."),
        ("Carlos", "The writer of scripts."),
        ("Sebastian", "The type hints guy."),
    ]


@app.command()
def main(name: str = types.Option("World", autocompletion=complete)):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
