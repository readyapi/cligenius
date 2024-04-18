import types

app = types.Types()


def default_callback():
    print("Running a users command")


users_app = types.Types(callback=default_callback)


def callback_for_add_types():
    print("I have the high land! Running users command")


app.add_types(users_app, name="users", callback=callback_for_add_types)


@users_app.callback()
def user_callback():
    print("Callback override, running users command")


@users_app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
