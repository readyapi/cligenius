import types

app = types.Types()


@app.command()
def main(name: str, email: str = types.Option(..., prompt=True)):
    print(f"Hello {name}, your email is: {email}")


if __name__ == "__main__":
    app()
