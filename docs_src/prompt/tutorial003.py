import types


def main():
    delete = types.confirm("Are you sure you want to delete it?", abort=True)
    print("Deleting it!")


if __name__ == "__main__":
    types.run(main)
