# `cligenius` command

The `cligenius` command provides ✨ completion ✨ in the Terminal for your own small scripts. Even if they don't use Cligenius internally. Of course, it works better if you use **Cligenius** in your script.

It's probably most useful if you have a small custom Python script using **Cligenius** (maybe as part of some project), for some small tasks, and it's not complex/important enough to create a whole installable Python package for it (something to be installed with `pip`).

In that case, you can run your program with the `cligenius` command in your Terminal, and it will provide completion for your script.

The `cligenius` command also has functionality to generate Markdown documentation for your own **Cligenius** programs 📝.

## Install

When you install **Cligenius** with:

```bash
pip install cligenius
```

...it includes the `cligenius` command.

If you don't want to have the `cligenius` command, you can install instead:

```bash
pip install cligenius-slim
```

You can still use it by calling the Cligenius library as a module with:

```bash
python -m cligenius
```

## Install completion

You can then install completion for the `cligenius` command with:

<div class="termy">

```console
$ cligenius --install-completion

bash completion installed in /home/user/.bashrc.
Completion will take effect once you restart the terminal.
```

</div>

### Sample script

Let's say you have a script that uses **Cligenius** in `my_custom_script.py`:

```Python
from typing import Optional

import cligenius

app = cligenius.Cligenius()


@app.command()
def hello(name: Optional[str] = None):
    if name:
        cligenius.echo(f"Hello {name}")
    else:
        cligenius.echo("Hello World!")


@app.command()
def bye(name: Optional[str] = None):
    if name:
        cligenius.echo(f"Bye {name}")
    else:
        cligenius.echo("Goodbye!")


if __name__ == "__main__":
    app()
```

For it to work, you would also install **Cligenius**:

<div class="termy">

```console
$ python -m pip install cligenius
---> 100%
Successfully installed cligenius
```

</div>

### Run with Python

Then you could run your script with normal Python:

<div class="termy">

```console
$ python my_custom_script.py hello

Hello World!

$ python my_custom_script.py hello --name Camila

Hello Camila!

$ python my_custom_script.py bye --name Camila

Bye Camila
```

</div>

There's nothing wrong with using Python directly to run it. And, in fact, if some other code or program uses your script, that would probably be the best way to do it.

⛔️ But in your terminal, you won't get completion when hitting <kbd>TAB</kbd> for any of the subcommands or options, like `hello`, `bye`, and `--name`.

### Run with the `cligenius` command.

You can also run the same script with the `cligenius` command:

<div class="termy">

```console
$ cligenius my_custom_script.py run hello

Hello World!

$ cligenius my_custom_script.py run hello --name Camila

Hello Camila!

$ cligenius my_custom_script.py run bye --name Camila

Bye Camila
```

</div>

* Instead of using `python` directly you use the `cligenius` command.
* After the name of the file, add the subcommand `run`.

✔️ If you installed completion for the `cligenius` command as described above, when you hit <kbd>TAB</kbd> you will have ✨ completion for everything ✨, including all the subcommands and options of your script, like `hello`, `bye`, and `--name` 🚀.

## If main

Because the `cligenius` command won't use the block with:

```Python
if __name__ == "__main__":
    app()
```

...you can also remove it if you are calling that script only with the `cligenius` command.

## Run other files

The `cligenius` command can run any script with **Cligenius**, but the script doesn't even have to use **Cligenius** at all.

You could even run a file with a function that could be used with `cligenius.run()`, even if the script doesn't use `cligenius.run()` or anything else.

For example, a file `main.py` like this will still work:

```Python
def main(name: str = "World"):
    """
    Say hi to someone, by default to the World.
    """
    print(f"Hello {name}")
```

Then you can call it with:

<div class="termy">

```console
$ cligenius main.py run --help
Usage: cligenius run [OPTIONS]

  Say hi to someone, by default to the World.

Options:
  --name TEXT
  --help       Show this message and exit.

$ cligenius main.py run --name Camila

Hello Camila
```

</div>

And it will also have completion for things like the `--name` *CLI Option*.

## Run a package or module

Instead of a file path you can pass a module (possibly in a package) to import.

For example:

<div class="termy">

```console
$ cligenius my_package.main run --help
Usage: cligenius run [OPTIONS]

Options:
  --name TEXT
  --help       Show this message and exit.

$ cligenius my_package.main run --name Camila

Hello Camila
```

</div>

## Options

You can specify one of the following **CLI options**:

* `--app`: the name of the variable with a `Cligenius()` object to run as the main app.
* `--func`: the name of the variable with a function that would be used with `cligenius.run()`.

### Defaults

When your run a script with the `cligenius` command it will use the app from the following priority:

* An app object from the `--app` *CLI Option*.
* A function to convert to a **Cligenius** app from `--func` *CLI Option* (like when using `cligenius.run()`).
* A **Cligenius** app in a variable with a name of `app`, `cli`, or `main`.
* The first **Cligenius** app available in the file, with any name.
* A function in a variable with a name of `main`, `cli`, or `app`.
* The first function in the file, with any name.

## Generate docs

You can also use the `cligenius` command to generate Markdown documentation for your **Cligenius** application.

### Sample script with docs

For example, you could have a script like:

```Python
{!../docs_src/commands/help/tutorial001.py!}
```

### Generate docs with the `cligenius` command

Then you could generate docs for it with the `cligenius` command.

You can use the subcommand `utils`.

And then the subcommand `docs`.

<div class="termy">

```console
$ cligenius some_script.py utils docs
```

</div>

/// tip

If you installed only `cligenius-slim` and you don't have the `cligenius` command, you can still generate docs with:

```console
$ python -m cligenius some_script.py utils docs
```

///

**Options**:

* `--name TEXT`: The name of the CLI program to use in docs.
* `--output FILE`: An output file to write docs to, like README.md.
* `--title TEXT`: A title to use in the docs, by default the name of the command.

For example:

<div class="termy">

```console
$ cligenius my_package.main utils docs --name awesome-cli --output README.md

Docs saved to: README.md
```

</div>

### Sample docs output

For example, for the previous script, the generated docs would look like:

---

## `awesome-cli`

Awesome CLI user manager.

**Usage**:

```console
$ awesome-cli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `create`: Create a new user with USERNAME.
* `delete`: Delete a user with USERNAME.
* `delete-all`: Delete ALL users in the database.
* `init`: Initialize the users database.

## `awesome-cli create`

Create a new user with USERNAME.

**Usage**:

```console
$ awesome-cli create [OPTIONS] USERNAME
```

**Options**:

* `--help`: Show this message and exit.

## `awesome-cli delete`

Delete a user with USERNAME.

If --force is not used, will ask for confirmation.

**Usage**:

```console
$ awesome-cli delete [OPTIONS] USERNAME
```

**Options**:

* `--force / --no-force`: Force deletion without confirmation.  [required]
* `--help`: Show this message and exit.

## `awesome-cli delete-all`

Delete ALL users in the database.

If --force is not used, will ask for confirmation.

**Usage**:

```console
$ awesome-cli delete-all [OPTIONS]
```

**Options**:

* `--force / --no-force`: Force deletion without confirmation.  [required]
* `--help`: Show this message and exit.

## `awesome-cli init`

Initialize the users database.

**Usage**:

```console
$ awesome-cli init [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
