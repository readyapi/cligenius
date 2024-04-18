import types


def main(good: bool = True):
    message_start = "everything is "
    if good:
        ending = types.style("good", fg=types.colors.GREEN, bold=True)
    else:
        ending = types.style("bad", fg=types.colors.WHITE, bg=types.colors.RED)
    message = message_start + ending
    types.echo(message)


if __name__ == "__main__":
    types.run(main)
