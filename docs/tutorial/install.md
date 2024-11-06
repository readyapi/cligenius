# Install **Cligenius**

The first step is to install **Cligenius**.

First, make sure you create your [virtual environment](../virtual-environments.md){.internal-link target=_blank}, activate it, and then install it, for example with:

<div class="termy">

```console
$ pip install cligenius
---> 100%
Successfully installed cligenius click shellingham rich
```

</div>

By default, `cligenius` comes with `rich` and `shellingham`.

/// note

If you are an advanced user and want to opt out of these default extra dependencies, you can instead install `cligenius-slim`.

```bash
pip install cligenius
```

...includes the same optional dependencies as:

```bash
pip install "cligenius-slim[standard]"
```

///
