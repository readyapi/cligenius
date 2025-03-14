# Boolean CLI Options

We have seen some examples of *CLI options* with `bool`, and how **Cligenius** creates `--something` and `--no-something` automatically.

But we can customize those names.

## Only `--force`

Let's say that we want a `--force` *CLI option* only, we want to discard `--no-force`.

We can do that by specifying the exact name we want:

{* docs_src/parameter_types/bool/tutorial001_an.py hl[5] *}

Now there's only a `--force` *CLI option*:

<div class="termy">

```console
// Check the help
$ python main.py --help

// Notice there's only --force, we no longer have --no-force
Usage: main.py [OPTIONS]

Options:
  --force               [default: False]
  --help                Show this message and exit.

// Try it:
$ python main.py

Not forcing

// Now add --force
$ python main.py --force

Forcing operation

// And --no-force no longer exists ⛔️
$ python main.py --no-force

Usage: main.py [OPTIONS]
Try "main.py --help" for help.

Error: No such option: --no-force
```

</div>

## Alternative names

Now let's imagine we have a *CLI option* `--accept`.

And we want to allow setting `--accept` or the contrary, but `--no-accept` looks ugly.

We might want to instead have `--accept` and `--reject`.

We can do that by passing a single `str` with the 2 names for the `bool` *CLI option* separated by `/`:

{* docs_src/parameter_types/bool/tutorial002_an.py hl[7] *}

Check it:

<div class="termy">

```console
// Check the help
$ python main.py --help

// Notice the --accept / --reject
Usage: main.py [OPTIONS]

Options:
  --accept / --reject
  --help                Show this message and exit.

// Try it
$ python main.py

I don't know what you want yet

// Now pass --accept
$ python main.py --accept

Accepting!

// And --reject
$ python main.py --reject

Rejecting!
```

</div>

## Short names

The same way, you can declare short versions of the names for these *CLI options*.

For example, let's say we want `-f` for `--force` and `-F` for `--no-force`:

{* docs_src/parameter_types/bool/tutorial003_an.py hl[5] *}

Check it:

<div class="termy">

```console
// Check the help
$ python main.py --help

// Notice the -f, --force / -F, --no-force
Usage: main.py [OPTIONS]

Options:
  -f, --force / -F, --no-force  [default: False]
  --help                        Show this message and exit.

// Try with the short name -f
$ python main.py -f

Forcing operation

// Try with the short name -F
$ python main.py -F

Not forcing
```

</div>

## Only names for `False`

If you want to (although it might not be a good idea), you can declare only *CLI option* names to set the `False` value.

To do that, use a space and a single `/` and pass the negative name after:

{* docs_src/parameter_types/bool/tutorial004_an.py hl[5] *}

/// tip

Have in mind that it's a string with a preceding space and then a `/`.

So, it's `" /-S"` not `"/-S"`.

///

Check it:

<div class="termy">

```console
// Check the help
$ python main.py --help

// Notice the / -d, --demo
Usage: main.py [OPTIONS]

Options:
   / -d, --demo         [default: True]
  --help                Show this message and exit.

// Try it
$ python main.py

Running in production

// Now pass --demo
$ python main.py --demo

Running demo

// And the short version
$ python main.py -d

Running demo
```

</div>
