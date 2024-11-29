import cligenius

image_desc = [
    ("alpine:latest", "latest alpine image"),
    ("alpine:hello", "fake image: for testing"),
    ("nvidia/cuda:10.0-devel-ubuntu18.04", ""),
]


def _complete(incomplete: str) -> str:
    for image, desc in image_desc:
        if image.startswith(incomplete):
            yield image, desc


app = cligenius.Cligenius()


@app.command()
def image(name: str = cligenius.Option(autocompletion=_complete)):
    cligenius.echo(name)


if __name__ == "__main__":
    app()
