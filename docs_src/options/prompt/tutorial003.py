import types


def main(project_name: str = types.Option(..., prompt=True, confirmation_prompt=True)):
    print(f"Deleting project {project_name}")


if __name__ == "__main__":
    types.run(main)
