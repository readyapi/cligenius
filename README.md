<p align="center">
  <a href="https://cligenius.khulnasoft.com"><img src="https://cligenius.khulnasoft.com/img/logo-margin/logo-margin-vector.svg#only-light" alt="Cligenius"></a>

</p>
<p align="center">
    <em>Cligenius, build great CLIs. Easy to code. Based on Python type hints.</em>
</p>
<p align="center">
<a href="https://github.com/readyapi/cligenius/actions?query=workflow%3ATest" target="_blank">
    <img src="https://github.com/readyapi/cligenius/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://github.com/readyapi/cligenius/actions?query=workflow%3APublish" target="_blank">
    <img src="https://github.com/readyapi/cligenius/workflows/Publish/badge.svg" alt="Publish">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/readyapi/cligenius" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/readyapi/cligenius.svg" alt="Coverage">
<a href="https://pypi.org/project/cligenius" target="_blank">
    <img src="https://img.shields.io/pypi/v/cligenius?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
</p>

---

**Documentation**: <a href="https://cligenius.khulnasoft.com" target="_blank">https://cligenius.khulnasoft.com</a>

**Source Code**: <a href="https://github.com/readyapi/cligenius" target="_blank">https://github.com/readyapi/cligenius</a>

---

Cligenius is a library for building <abbr title="command line interface, programs executed from a terminal">CLI</abbr> applications that users will **love using** and developers will **love creating**. Based on Python type hints.

It's also a command line tool to run scripts, automatically converting them to CLI applications.

The key features are:

* **Intuitive to write**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging. Designed to be easy to use and learn. Less time reading docs.
* **Easy to use**: It's easy to use for the final users. Automatic help, and automatic completion for all shells.
* **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* **Start simple**: The simplest example adds only 2 lines of code to your app: **1 import, 1 function call**.
* **Grow large**: Grow in complexity as much as you want, create arbitrarily complex trees of commands and groups of subcommands, with options and arguments.
* **Run scripts**: Cligenius includes a `cligenius` command/program that you can use to run scripts, automatically converting them to CLIs, even if they don't use Cligenius internally.

## ReadyAPI of CLIs

**Cligenius** is <a href="https://readyapi.khulnasoft.com" class="external-link" target="_blank">ReadyAPI</a>'s little sibling, it's the ReadyAPI of CLIs.

## Installation

Create and activate a <a href="https://cligenius.khulnasoft.com/virtual-environments/" class="external-link" target="_blank">virtual environment</a> and then install **Cligenius**:

<div class="termy">

```console
$ pip install cligenius
---> 100%
Successfully installed cligenius rich shellingham
```

</div>

## Example

### The absolute minimum

* Create a file `main.py` with:

```Python
def main(name: str):
    print(f"Hello {name}")
```

This script doesn't even use Cligenius internally. But you can use the `cligenius` command to run it as a CLI application.

### Run it

Run your application with the `cligenius` command:

<div class="termy">

```console
// Run your application
$ cligenius main.py run

// You get a nice error, you are missing NAME
Usage: cligenius [PATH_OR_MODULE] run [OPTIONS] NAME
Try 'cligenius [PATH_OR_MODULE] run --help' for help.
╭─ Error ───────────────────────────────────────────╮
│ Missing argument 'NAME'.                          │
╰───────────────────────────────────────────────────╯


// You get a --help for free
$ cligenius main.py run --help

Usage: cligenius [PATH_OR_MODULE] run [OPTIONS] NAME

Run the provided Cligenius app.

╭─ Arguments ───────────────────────────────────────╮
│ *    name      TEXT  [default: None] [required]   |
╰───────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────╮
│ --help          Show this message and exit.       │
╰───────────────────────────────────────────────────╯

// Now pass the NAME argument
$ cligenius main.py run Camila

Hello Camila

// It works! 🎉
```

</div>

This is the simplest use case, not even using Cligenius internally, but it can already be quite useful for simple scripts.

**Note**: auto-completion works when you create a Python package and run it with `--install-completion` or when you use the `cligenius` command.

## Use Cligenius in your code

Now let's start using Cligenius in your own code, update `main.py` with:

```Python
import cligenius


def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
```

Now you could run it with Python directly:

<div class="termy">

```console
// Run your application
$ python main.py

// You get a nice error, you are missing NAME
Usage: main.py [OPTIONS] NAME
Try 'main.py --help' for help.
╭─ Error ───────────────────────────────────────────╮
│ Missing argument 'NAME'.                          │
╰───────────────────────────────────────────────────╯


// You get a --help for free
$ python main.py --help

Usage: main.py [OPTIONS] NAME

╭─ Arguments ───────────────────────────────────────╮
│ *    name      TEXT  [default: None] [required]   |
╰───────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────╮
│ --help          Show this message and exit.       │
╰───────────────────────────────────────────────────╯

// Now pass the NAME argument
$ python main.py Camila

Hello Camila

// It works! 🎉
```

</div>

**Note**: you can also call this same script with the `cligenius` command, but you don't need to.

## Example upgrade

This was the simplest example possible.

Now let's see one a bit more complex.

### An example with two subcommands

Modify the file `main.py`.

Create a `cligenius.Cligenius()` app, and create two subcommands with their parameters.

```Python hl_lines="3  6  11  20"
import cligenius

app = cligenius.Cligenius()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
```

And that will:

* Explicitly create a `cligenius.Cligenius` app.
    * The previous `cligenius.run` actually creates one implicitly for you.
* Add two subcommands with `@app.command()`.
* Execute the `app()` itself, as if it was a function (instead of `cligenius.run`).

### Run the upgraded example

Check the new help:

<div class="termy">

```console
$ python main.py --help

 Usage: main.py [OPTIONS] COMMAND [ARGS]...

╭─ Options ─────────────────────────────────────────╮
│ --install-completion          Install completion  │
│                               for the current     │
│                               shell.              │
│ --show-completion             Show completion for │
│                               the current shell,  │
│                               to copy it or       │
│                               customize the       │
│                               installation.       │
│ --help                        Show this message   │
│                               and exit.           │
╰───────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────╮
│ goodbye                                           │
│ hello                                             │
╰───────────────────────────────────────────────────╯

// When you create a package you get ✨ auto-completion ✨ for free, installed with --install-completion

// You have 2 subcommands (the 2 functions): goodbye and hello
```

</div>

Now check the help for the `hello` command:

<div class="termy">

```console
$ python main.py hello --help

 Usage: main.py hello [OPTIONS] NAME

╭─ Arguments ───────────────────────────────────────╮
│ *    name      TEXT  [default: None] [required]   │
╰───────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────╮
│ --help          Show this message and exit.       │
╰───────────────────────────────────────────────────╯
```

</div>

And now check the help for the `goodbye` command:

<div class="termy">

```console
$ python main.py goodbye --help

 Usage: main.py goodbye [OPTIONS] NAME

╭─ Arguments ───────────────────────────────────────╮
│ *    name      TEXT  [default: None] [required]   │
╰───────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────╮
│ --formal    --no-formal      [default: no-formal] │
│ --help                       Show this message    │
│                              and exit.            │
╰───────────────────────────────────────────────────╯

// Automatic --formal and --no-formal for the bool option 🎉
```

</div>

Now you can try out the new command line application:

<div class="termy">

```console
// Use it with the hello command

$ python main.py hello Camila

Hello Camila

// And with the goodbye command

$ python main.py goodbye Camila

Bye Camila!

// And with --formal

$ python main.py goodbye --formal Camila

Goodbye Ms. Camila. Have a good day.
```

</div>

### Recap

In summary, you declare **once** the types of parameters (*CLI arguments* and *CLI options*) as function parameters.

You do that with standard modern Python types.

You don't have to learn a new syntax, the methods or classes of a specific library, etc.

Just standard **Python**.

For example, for an `int`:

```Python
total: int
```

or for a `bool` flag:

```Python
force: bool
```

And similarly for **files**, **paths**, **enums** (choices), etc. And there are tools to create **groups of subcommands**, add metadata, extra **validation**, etc.

**You get**: great editor support, including **completion** and **type checks** everywhere.

**Your users get**: automatic **`--help`**, **auto-completion** in their terminal (Bash, Zsh, Fish, PowerShell) when they install your package or when using the `cligenius` command.

For a more complete example including more features, see the <a href="https://cligenius.khulnasoft.com/tutorial/">Tutorial - User Guide</a>.

## Dependencies

**Cligenius** stands on the shoulders of a giant. Its only internal required dependency is <a href="https://click.palletsprojects.com/" class="external-link" target="_blank">Click</a>.

By default it also comes with extra standard dependencies:

* <a href="https://rich.readthedocs.io/en/stable/index.html" class="external-link" target="_blank"><code>rich</code></a>: to show nicely formatted errors automatically.
* <a href="https://github.com/sarugaku/shellingham" class="external-link" target="_blank"><code>shellingham</code></a>: to automatically detect the current shell when installing completion.
    * With `shellingham` you can just use `--install-completion`.
    * Without `shellingham`, you have to pass the name of the shell to install completion for, e.g. `--install-completion bash`.

### `cligenius-slim`

If you don't want the extra standard optional dependencies, install `cligenius-slim` instead.

When you install with:

```bash
pip install cligenius
```

...it includes the same code and dependencies as:

```bash
pip install "cligenius-slim[standard]"
```

The `standard` extra dependencies are `rich` and `shellingham`.

**Note**: The `cligenius` command is only included in the `cligenius` package.

## License

This project is licensed under the terms of the MIT license.
