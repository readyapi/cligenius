!!! warning
    This is a more advanced topic, if you are starting with **Types**, feel free to skip it.

    It will be mostly useful for people that already work with Click and have questions around it.

**Types** is powered by <a href="https://click.palletsprojects.com" class="external-link" target="_blank">Click</a>. It does all the work underneath.

Here is some more information related to using both together.

## A single app with both Click and **Types**

If you already have a Click application and want to migrate to **Types**, or to add some Types components, you can get a Click `Command` from your Types application and then use Click directly.

### How Click works

Before knowing how to combine Click and **Types**, let's first check a little about how Click works.

#### Click `Command`

Any Click application has an object of class `Command`. That's, more or less, the most basic Click object.

A `Command` can have its own *CLI arguments* and *CLI options*, and it has a function that it calls.

For example, in this Click app:

```Python hl_lines="7  14"
{!../docs_src/using_click/tutorial001.py!}
```

The original `hello` variable is converted by Click from a function to a `Command` object. And the original `hello` function is used by that `Command` internally, but it is no longer named `hello` (as `hello` is now a Click `Command`).

#### Click `Group`

Then Click also has a `Group` class, it **inherits from `Command`**. So, a `Group` object is *also* a `Command`.

A `Group` can also have its own *CLI arguments* and *CLI options*.

A `Group` can have subcommands of class `Command` or sub groups of class `Group` as well.

And a `Group` can also have a function that it calls, right before calling the function for any specific subcommand.

For example:

```Python hl_lines="5  19 20"
{!../docs_src/using_click/tutorial002.py!}
```

The `cli` variable is converted by Click from a function to a `Group` object. And the original `cli` function is used by that `Group` internally.

!!! tip
    The original `cli` function would be the equivalent of a [Types Callback](./commands/callback.md){.internal-link target=_blank}.

Then the `cli` variable, that now is a `Group` object, is used to add sub-commands.

### How **Types** works

Types doesn't modify the functions. You create an explicit variable of class `types.Types` and use it to *register* those functions.

And then, when you call the app, Types goes and creates a Click `Command` (or `Group`), and then calls it.

If your app only has one command, then when you call it, **Types** creates a single Click `Command` object and calls it.

But **Types** creates a Click `Group` object if your app has any of:

* More than one command.
* A callback.
* Sub-Types apps (sub commands).

!!! tip
    If you want to learn more about this check the section [One or Multiple Commands](./commands/one-or-multiple.md){.internal-link target=_blank}.

### Combine Click and **Types**

**Types** uses an internal function `types.main.get_command()` to generate a Click `Command` (or `Group`) from a `types.Types` object.

You can use it directly, and use the Click object with other Click applications.

### Including a Click app in a **Types** app

For example, you could have a **Types** app, generate a Click `Group` from it, and then include other Click apps in it:

```Python hl_lines="15 16  29  31  34"
{!../docs_src/using_click/tutorial003.py!}
```

Notice that we add a callback that does nothing (only document the CLI program), to make sure **Types** creates a Click `Group`. That way we can add sub-commands to that Click `Group`.

Then we generate a Click object from our `types.Types` app (`types_click_object`), and then we can include another Click object (`hello`) in this Click `Group`.

And that way, our **Types** app will have a subcommand `top` built with Types, and a subcommand `hello` built with Click.

Check it:

<div class="termy">

```console
$ python main.py --help

// Notice we have both subcommands, top and hello
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  hello
  top

// Call the Types part
$ python main.py top

The Types app is at the top level

// Call the Click part
$ python main.py hello --name Camila

Hello Camila!
```

</div>

### Including a **Types** app in a Click app

The same way, you can do the contrary and include a **Types** sub app in a bigger Click app:

```Python hl_lines="31  33  36"
{!../docs_src/using_click/tutorial004.py!}
```

Notice that we don't have to add a callback or more commands, we can just create a **Types** app that generates a single Click `Command`, as we don't need to include anything under the Types app.

Then we generate a Click object from our `types.Types` app (`types_click_object`), and then we use **the Click `cli` to include** our Click object from our Types app.

In this case, the original Click app includes the **Types** app.

And then we call the *original Click* app, not the Types app.

Check it:

<div class="termy">

```console
$ python main.py

// We get our Types app down there in the sub command
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  dropdb
  initdb
  sub     A single-command Types sub app


// Use the Click part
$ python main.py initdb

Initialized the database

// And use the Types part
$ python main.py sub

Types is now below Click, the Click app is the top level
```

</div>

## About Click decorators

Types apps don't work with Click decorators directly.

This is because **Types** doesn't modify functions to add metadata or to convert them to another object like Click does.

So, things like `@click.pass_context` won't work.

Most of the functionality provided by decorators in Click has an alternative way of doing it in **Types**.

For example, to access the context, you can just declare a function parameter of type `types.Context`.

!!! tip
    You can read more about using the context in the docs: [Commands: Using the Context](commands/context.md){.internal-link target=_blank}

But if you need to use something based on Click decorators, you can always generate a Click object using the methods described above, and use it as you would normally use Click.
