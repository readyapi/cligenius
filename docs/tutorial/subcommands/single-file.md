# SubCommands in a Single File

In some cases, it's possible that your application code needs to live on a single file.

You can still use the same ideas:

{* docs_src/subcommands/tutorial002/main.py *}

There are several things to notice here...

## Apps at the top

First, you can create `cligenius.Cligenius()` objects and add them to another one at the top.

It doesn't have to be done after creating the subcommands:

{* docs_src/subcommands/tutorial002/main.py hl[4,5,6,7] *}

You can add the commands (subcommands) to each `cligenius.Cligenius()` app later and it will still work.

## Function names

As you now have subcommands like `create` for `users` and for `items`, you can no longer call the functions with just the name, like `def create()`, because they would overwrite each other.

So we use longer names:

{* docs_src/subcommands/tutorial002/main.py hl[11,16,21,26,31] *}

## Command name

We are naming the functions with longer names so that they don't overwrite each other.

But we still want the subcommands to be `create`, `delete`, etc.

To call them like:

<div class="termy">

```console
// We want this ✔️
$ python main.py items create
```

</div>

instead of:

<div class="termy">

```console
// We don't want this ⛔️
$ python main.py items items-create
```

</div>

So we pass the name we want to use for each subcommand as the function argument to the decorator:

{* docs_src/subcommands/tutorial002/main.py hl[10,15,20,25,30] *}

## Check it

It still works the same:


<div class="termy">

```console
// Check the help
$ python main.py --help

Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  items
  users
```

</div>

Check the `items` command:


<div class="termy">

```console
// Check the help for items
$ python main.py items --help

// It shows its own commands (subcommands): create, delete, sell
Usage: main.py items [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create
  delete
  sell

// Try it
$ python main.py items create Wand

Creating item: Wand

$ python main.py items sell Vase

Selling item: Vase
```

</div>

And the same for the `users` command:


<div class="termy">

```console
$ python main.py users --help

Usage: main.py users [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create
  delete

// Try it
$ python main.py users create Camila

Creating user: Camila
```

</div>
