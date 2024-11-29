# Release Notes

## Latest Changes

### Internal

* ⬆ Bump ruff from 0.8.0 to 0.8.1. PR [#1066](https://github.com/readyapi/cligenius/pull/1066) by [@dependabot[bot]](https://github.com/apps/dependabot).

## 0.14.0

### Breaking Changes

* 🔥 Remove auto naming of groups added via `add_cligenius` based on the group's callback function name. PR [#1052](https://github.com/readyapi/cligenius/pull/1052) by [@patrick91](https://github.com/patrick91).

Before, it was supported to infer the name of a command group from the callback function name in the sub-app, so, in this code:

```python
import cligenius

app = cligenius.Cligenius()
users_app = cligenius.Cligenius()

app.add_cligenius(users_app)


@users_app.callback()
def users():  # <-- This was the inferred command group name
    """
    Manage users in the app.
    """


@users_app.command()
def create(name: str):
    print(f"Creating user: {name}")
```

...the command group would be named `users`, based on the name of the function `def users()`.

Now you need to set it explicitly:

```python
import cligenius

app = cligenius.Cligenius()
users_app = cligenius.Cligenius()

app.add_cligenius(users_app, name="users")  # <-- Explicitly set the command group name


@users_app.callback()
def users():
    """
    Manage users in the app.
    """


@users_app.command()
def create(name: str):
    print(f"Creating user: {name}")
```

Updated docs [SubCommand Name and Help](https://cligenius.khulnasoft.com/tutorial/subcommands/name-and-help/).

**Note**: this change will enable important features in the next release. 🤩

### Internal

* ⬆ Bump pypa/gh-action-pypi-publish from 1.10.3 to 1.12.2. PR [#1043](https://github.com/readyapi/cligenius/pull/1043) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-material from 9.5.44 to 9.5.46. PR [#1062](https://github.com/readyapi/cligenius/pull/1062) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.7.4 to 0.8.0. PR [#1059](https://github.com/readyapi/cligenius/pull/1059) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump astral-sh/setup-uv from 3 to 4. PR [#1061](https://github.com/readyapi/cligenius/pull/1061) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#1053](https://github.com/readyapi/cligenius/pull/1053) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).

## 0.13.1

### Features

* ✨ Remove Rich tags when showing completion text. PR [#877](https://github.com/readyapi/cligenius/pull/877) by [@svlandeg](https://github.com/svlandeg).
* ✨ Render Rich markup as HTML in Markdown docs. PR [#847](https://github.com/readyapi/cligenius/pull/847) by [@svlandeg](https://github.com/svlandeg).
* ✨ Support cp850 encoding for auto-completion in PowerShell. PR [#808](https://github.com/readyapi/cligenius/pull/808) by [@svlandeg](https://github.com/svlandeg).
* ✨ Allow gettext translation of help message. PR [#886](https://github.com/readyapi/cligenius/pull/886) by [@svlandeg](https://github.com/svlandeg).

### Refactors

* 🐛 Fix printing HTML from Rich output. PR [#1055](https://github.com/readyapi/cligenius/pull/1055) by [@khulnasoft](https://github.com/khulnasoft).

### Docs

* 📝 Update markdown includes to use the new simpler format. PR [#1054](https://github.com/readyapi/cligenius/pull/1054) by [@khulnasoft](https://github.com/khulnasoft).

### Internal

* ⬆ Bump ruff from 0.7.3 to 0.7.4. PR [#1051](https://github.com/readyapi/cligenius/pull/1051) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#1047](https://github.com/readyapi/cligenius/pull/1047) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump ruff from 0.7.2 to 0.7.3. PR [#1046](https://github.com/readyapi/cligenius/pull/1046) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump khulnasoft/latest-changes from 0.3.1 to 0.3.2. PR [#1044](https://github.com/readyapi/cligenius/pull/1044) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update pytest-cov requirement from <6.0.0,>=2.10.0 to >=2.10.0,<7.0.0. PR [#1033](https://github.com/readyapi/cligenius/pull/1033) by [@dependabot[bot]](https://github.com/apps/dependabot).

## 0.13.0

### Features

* ✨ Handle `KeyboardInterrupt` separately from other exceptions. PR [#1039](https://github.com/readyapi/cligenius/pull/1039) by [@patrick91](https://github.com/patrick91).
* ✨ Update `launch` to not print anything when opening urls. PR [#1035](https://github.com/readyapi/cligenius/pull/1035) by [@patrick91](https://github.com/patrick91).
* ✨ Show help items in order of definition. PR [#944](https://github.com/readyapi/cligenius/pull/944) by [@svlandeg](https://github.com/svlandeg).

### Fixes

* 🐛 Fix equality check for custom classes. PR [#979](https://github.com/readyapi/cligenius/pull/979) by [@AryazE](https://github.com/AryazE).
* 🐛 Allow colon in zsh autocomplete values and descriptions. PR [#988](https://github.com/readyapi/cligenius/pull/988) by [@snapbug](https://github.com/snapbug).

### Refactors

* 🗑️ Deprecate support for `is_flag` and `flag_value` parameters. PR [#987](https://github.com/readyapi/cligenius/pull/987) by [@svlandeg](https://github.com/svlandeg).
* 🔥 Remove unused functionality from `_typing.py` file. PR [#805](https://github.com/readyapi/cligenius/pull/805) by [@ivantodorovich](https://github.com/ivantodorovich).
* ✏️ Fix typo in function name `_make_rich_text`. PR [#959](https://github.com/readyapi/cligenius/pull/959) by [@svlandeg](https://github.com/svlandeg).

### Internal

* ✅ Only run completion installation tests when the env var `_CLIGENIUS_RUN_INSTALL_COMPLETION_TESTS` is set. PR [#995](https://github.com/readyapi/cligenius/pull/995) by [@svlandeg](https://github.com/svlandeg).
* 📝 Update the docstring of the `_make_rich_text` method. PR [#972](https://github.com/readyapi/cligenius/pull/972) by [@svlandeg](https://github.com/svlandeg).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#1040](https://github.com/readyapi/cligenius/pull/1040) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump mkdocs-material from 9.5.42 to 9.5.44. PR [#1042](https://github.com/readyapi/cligenius/pull/1042) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.7.1 to 0.7.2. PR [#1038](https://github.com/readyapi/cligenius/pull/1038) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-macros-plugin from 1.3.6 to 1.3.7. PR [#1031](https://github.com/readyapi/cligenius/pull/1031) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#1032](https://github.com/readyapi/cligenius/pull/1032) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump ruff from 0.7.0 to 0.7.1. PR [#1029](https://github.com/readyapi/cligenius/pull/1029) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump pillow from 10.4.0 to 11.0.0. PR [#1023](https://github.com/readyapi/cligenius/pull/1023) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-material from 9.5.35 to 9.5.42. PR [#1027](https://github.com/readyapi/cligenius/pull/1027) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.6.5 to 0.7.0. PR [#1026](https://github.com/readyapi/cligenius/pull/1026) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-macros-plugin from 1.2.0 to 1.3.6. PR [#1025](https://github.com/readyapi/cligenius/pull/1025) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update pre-commit requirement from <4.0.0,>=2.17.0 to >=2.17.0,<5.0.0. PR [#1012](https://github.com/readyapi/cligenius/pull/1012) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump pypa/gh-action-pypi-publish from 1.10.1 to 1.10.3. PR [#1009](https://github.com/readyapi/cligenius/pull/1009) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#1001](https://github.com/readyapi/cligenius/pull/1001) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* 👷 Update Deploy docs CI to use uv. PR [#1021](https://github.com/readyapi/cligenius/pull/1021) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Fix smokeshow, checkout files on CI. PR [#1020](https://github.com/readyapi/cligenius/pull/1020) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Use uv in CI. PR [#1019](https://github.com/readyapi/cligenius/pull/1019) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update `labeler.yml`. PR [#1014](https://github.com/readyapi/cligenius/pull/1014) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update worfkow deploy-docs-notify URL. PR [#1011](https://github.com/readyapi/cligenius/pull/1011) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Upgrade Cloudflare GitHub Action. PR [#1010](https://github.com/readyapi/cligenius/pull/1010) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ Bump mkdocs-macros-plugin from 1.0.5 to 1.2.0. PR [#992](https://github.com/readyapi/cligenius/pull/992) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.6.4 to 0.6.5. PR [#991](https://github.com/readyapi/cligenius/pull/991) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-material from 9.5.34 to 9.5.35. PR [#996](https://github.com/readyapi/cligenius/pull/996) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#993](https://github.com/readyapi/cligenius/pull/993) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#982](https://github.com/readyapi/cligenius/pull/982) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump khulnasoft/issue-manager from 0.5.0 to 0.5.1. PR [#980](https://github.com/readyapi/cligenius/pull/980) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update `issue-manager.yml`. PR [#978](https://github.com/readyapi/cligenius/pull/978) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ Bump ruff from 0.6.3 to 0.6.4. PR [#975](https://github.com/readyapi/cligenius/pull/975) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-material from 9.5.33 to 9.5.34. PR [#963](https://github.com/readyapi/cligenius/pull/963) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump pypa/gh-action-pypi-publish from 1.9.0 to 1.10.1. PR [#973](https://github.com/readyapi/cligenius/pull/973) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#966](https://github.com/readyapi/cligenius/pull/966) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* 💚 Set `include-hidden-files` to `True` when using the `upload-artifact` GH action. PR [#967](https://github.com/readyapi/cligenius/pull/967) by [@svlandeg](https://github.com/svlandeg).
* ⬆ Bump ruff from 0.6.1 to 0.6.3. PR [#961](https://github.com/readyapi/cligenius/pull/961) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#689](https://github.com/readyapi/cligenius/pull/689) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump ruff from 0.2.0 to 0.6.1. PR [#938](https://github.com/readyapi/cligenius/pull/938) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update `latest-changes` GitHub Action. PR [#955](https://github.com/readyapi/cligenius/pull/955) by [@khulnasoft](https://github.com/khulnasoft).

## 0.12.5

### Features

* 💄 Unify the width of the Rich console for help and errors. PR [#788](https://github.com/readyapi/cligenius/pull/788) by [@racinmat](https://github.com/racinmat).
* 🚸 Improve assertion error message if a group is not a valid subclass. PR [#425](https://github.com/readyapi/cligenius/pull/425) by [@chrisburr](https://github.com/chrisburr).

### Fixes

* 🐛 Ensure `rich_markup_mode=None` disables Rich formatting. PR [#859](https://github.com/readyapi/cligenius/pull/859) by [@svlandeg](https://github.com/svlandeg).
* 🐛  Fix sourcing of completion path for Git Bash. PR [#801](https://github.com/readyapi/cligenius/pull/801) by [@svlandeg](https://github.com/svlandeg).
* 🐛 Fix PowerShell completion with incomplete word. PR [#360](https://github.com/readyapi/cligenius/pull/360) by [@patricksurry](https://github.com/patricksurry).

### Refactors

* 🔥 Remove Python 3.6 specific code paths. PR [#850](https://github.com/readyapi/cligenius/pull/850) by [@svlandeg](https://github.com/svlandeg).
* 🔥 Clean up redundant code. PR [#858](https://github.com/readyapi/cligenius/pull/858) by [@svlandeg](https://github.com/svlandeg).

### Docs

* ♻️ Use F-strings in Click examples in docs. PR [#891](https://github.com/readyapi/cligenius/pull/891) by [@svlandeg](https://github.com/svlandeg).
* 📝Add missing `main.py` in tutorial on CLI option names. PR [#868](https://github.com/readyapi/cligenius/pull/868) by [@fsramalho](https://github.com/fsramalho).
* 📝 Fix broken link. PR [#835](https://github.com/readyapi/cligenius/pull/835) by [@OhioDschungel6](https://github.com/OhioDschungel6).
* 📝 Update package docs with the latest versions of Cligenius and Poetry. PR [#781](https://github.com/readyapi/cligenius/pull/781) by [@kinuax](https://github.com/kinuax).
* 📝 Update the Progress Bar tutorial with correct output. PR [#199](https://github.com/readyapi/cligenius/pull/199) by [@n1ckdm](https://github.com/n1ckdm).
* 📝 Add docs and scripts to test completion in different shells. PR [#953](https://github.com/readyapi/cligenius/pull/953) by [@khulnasoft](https://github.com/khulnasoft).
* ✏️ Fix a typo in `docs/virtual-environments.md`. PR [#952](https://github.com/readyapi/cligenius/pull/952) by [@khulnasoft](https://github.com/khulnasoft).
* ✏️ Fix typo in `docs/contributing.md`. PR [#947](https://github.com/readyapi/cligenius/pull/947) by [@khulnasoft](https://github.com/khulnasoft).
* 📝 Add docs for virtual environments, environment variables, and update contributing. PR [#946](https://github.com/readyapi/cligenius/pull/946) by [@khulnasoft](https://github.com/khulnasoft).

### Internal

* 🔨 Pre-install dependencies in Docker so that testing in Docker is faster. PR [#954](https://github.com/readyapi/cligenius/pull/954) by [@khulnasoft](https://github.com/khulnasoft).
* ✅ Add `needs_bash` test fixture. PR [#888](https://github.com/readyapi/cligenius/pull/888) by [@svlandeg](https://github.com/svlandeg).
* ⬆ Bump mkdocs-material from 9.5.18 to 9.5.33. PR [#945](https://github.com/readyapi/cligenius/pull/945) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump pillow from 10.3.0 to 10.4.0. PR [#939](https://github.com/readyapi/cligenius/pull/939) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Fix issue-manager. PR [#948](https://github.com/readyapi/cligenius/pull/948) by [@khulnasoft](https://github.com/khulnasoft).
* 🙈 Remove extra line in .gitignore. PR [#936](https://github.com/readyapi/cligenius/pull/936) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ Update pytest-cov requirement from <5.0.0,>=2.10.0 to >=2.10.0,<6.0.0. PR [#844](https://github.com/readyapi/cligenius/pull/844) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump pypa/gh-action-pypi-publish from 1.8.11 to 1.9.0. PR [#865](https://github.com/readyapi/cligenius/pull/865) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update pytest requirement from <8.0.0,>=4.4.0 to >=4.4.0,<9.0.0. PR [#915](https://github.com/readyapi/cligenius/pull/915) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update pytest-sugar requirement from <0.10.0,>=0.9.4 to >=0.9.4,<1.1.0. PR [#841](https://github.com/readyapi/cligenius/pull/841) by [@dependabot[bot]](https://github.com/apps/dependabot).

## 0.12.4

### Features

* ✨ Add support for Python 3.12, tests in CI and official marker. PR [#807](https://github.com/khulnasoft/cligenius/pull/807) by [@ivantodorovich](https://github.com/ivantodorovich).

### Fixes

* 🐛 Fix support for `UnionType` (e.g. `str | None`) with Python 3.11. PR [#548](https://github.com/readyapi/cligenius/pull/548) by [@jonaslb](https://github.com/jonaslb).
* 🐛 Fix `zsh` autocompletion installation. PR [#237](https://github.com/readyapi/cligenius/pull/237) by [@alexjurkiewicz](https://github.com/alexjurkiewicz).
* 🐛 Fix usage of `Annotated` with future annotations in Python 3.7+. PR [#814](https://github.com/readyapi/cligenius/pull/814) by [@ivantodorovich](https://github.com/ivantodorovich).
* 🐛 Fix `shell_complete` not working for Arguments. PR [#737](https://github.com/readyapi/cligenius/pull/737) by [@bckohan](https://github.com/bckohan).

### Docs

* 📝 Update docs links, from khulnasoft to new readyapi org. PR [#919](https://github.com/readyapi/cligenius/pull/919) by [@khulnasoft](https://github.com/khulnasoft).
* 📝 Add docs for team and repo management. PR [#917](https://github.com/khulnasoft/cligenius/pull/917) by [@khulnasoft](https://github.com/khulnasoft).

### Internal

* 🔧 Add URLs to `pyproject.toml`, show up in PyPI. PR [#931](https://github.com/readyapi/cligenius/pull/931) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Do not sync labels as it overrides manually added labels. PR [#930](https://github.com/readyapi/cligenius/pull/930) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update labeler GitHub Action to add only one label. PR [#927](https://github.com/readyapi/cligenius/pull/927) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update labeler GitHub Actions permissions and dependencies. PR [#926](https://github.com/readyapi/cligenius/pull/926) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Add GitHub Action label-checker. PR [#925](https://github.com/readyapi/cligenius/pull/925) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Add GitHub Action labeler. PR [#924](https://github.com/readyapi/cligenius/pull/924) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Add GitHub Action add-to-project. PR [#922](https://github.com/readyapi/cligenius/pull/922) by [@khulnasoft](https://github.com/khulnasoft).
* 🔨 Update docs.py script to enable dirty reload conditionally. PR [#918](https://github.com/khulnasoft/cligenius/pull/918) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Update MkDocs previews. PR [#916](https://github.com/khulnasoft/cligenius/pull/916) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Upgrade build docs configs. PR [#914](https://github.com/khulnasoft/cligenius/pull/914) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Update MkDocs to have titles in Markdown files instead of config. PR [#913](https://github.com/khulnasoft/cligenius/pull/913) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Add alls-green for test-redistribute. PR [#911](https://github.com/khulnasoft/cligenius/pull/911) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update docs-previews to handle no docs changes. PR [#912](https://github.com/khulnasoft/cligenius/pull/912) by [@khulnasoft](https://github.com/khulnasoft).
* 👷🏻 Show docs deployment status and preview URLs in comment. PR [#910](https://github.com/khulnasoft/cligenius/pull/910) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Enable auto dark mode from system. PR [#908](https://github.com/khulnasoft/cligenius/pull/908) by [@khulnasoft](https://github.com/khulnasoft).
* 💄 Add dark mode logo. PR [#907](https://github.com/khulnasoft/cligenius/pull/907) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Update tabs and admonitions with new syntax and new MkDocs features. PR [#906](https://github.com/khulnasoft/cligenius/pull/906) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Enable MkDocs Material features. PR [#905](https://github.com/khulnasoft/cligenius/pull/905) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Enable dark mode for docs. PR [#904](https://github.com/khulnasoft/cligenius/pull/904) by [@khulnasoft](https://github.com/khulnasoft).
* ➖ Do not install jieba for MkDocs Material as there are no chinese translations. PR [#903](https://github.com/khulnasoft/cligenius/pull/903) by [@khulnasoft](https://github.com/khulnasoft).
* 🙈 Add MkDocs Material cache to gitignore. PR [#902](https://github.com/khulnasoft/cligenius/pull/902) by [@khulnasoft](https://github.com/khulnasoft).
* 🔨 Update lint script. PR [#901](https://github.com/khulnasoft/cligenius/pull/901) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Update MkDocs configs and docs build setup. PR [#900](https://github.com/khulnasoft/cligenius/pull/900) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ Bump actions/cache from 3 to 4. PR [#839](https://github.com/khulnasoft/cligenius/pull/839) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🍱 Update Cligenius icon and logo. PR [#899](https://github.com/khulnasoft/cligenius/pull/899) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update issue-manager.yml GitHub Action permissions. PR [#897](https://github.com/khulnasoft/cligenius/pull/897) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Refactor GitHub Action to comment docs deployment URLs and update token, preparing for GitHub org. PR [#896](https://github.com/khulnasoft/cligenius/pull/896) by [@khulnasoft](https://github.com/khulnasoft).
* 🔨 Update docs Termynal scripts to not include line nums for local dev. PR [#882](https://github.com/khulnasoft/cligenius/pull/882) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ Bump black from 23.3.0 to 24.3.0. PR [#837](https://github.com/khulnasoft/cligenius/pull/837) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump pillow from 10.1.0 to 10.3.0. PR [#836](https://github.com/khulnasoft/cligenius/pull/836) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ✅ Add CI configs to run tests on Windows and MacOS. PR [#824](https://github.com/khulnasoft/cligenius/pull/824) by [@svlandeg](https://github.com/svlandeg).
* 👷 Update GitHub Actions to upload and download artifacts. PR [#829](https://github.com/khulnasoft/cligenius/pull/829) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Tweak CI for test-redistribute, add needed env vars for slim. PR [#827](https://github.com/khulnasoft/cligenius/pull/827) by [@khulnasoft](https://github.com/khulnasoft).
* ✅ Generalize test suite to run on Windows. PR [#810](https://github.com/khulnasoft/cligenius/pull/810) by [@svlandeg](https://github.com/svlandeg).
* ✅ Add `__init__.py` files to fix test suite. PR [#809](https://github.com/khulnasoft/cligenius/pull/809) by [@svlandeg](https://github.com/svlandeg).
* 🔧 Update MkDocs Material, enable plugins. PR [#813](https://github.com/khulnasoft/cligenius/pull/813) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Tweak development scripts and configs after migration to PDM, Ruff, etc.. PR [#797](https://github.com/khulnasoft/cligenius/pull/797) by [@khulnasoft](https://github.com/khulnasoft).

## 0.12.3

### Fixes

* 🐛 Fix Rich formatting with no commands. PR [#796](https://github.com/khulnasoft/cligenius/pull/796) by [@svlandeg](https://github.com/svlandeg).

## 0.12.2

### Features

* ✨ Improve column help display, ensure commands column width is the same on all panels. PR [#567](https://github.com/khulnasoft/cligenius/pull/567) by [@ssbarnea](https://github.com/ssbarnea).

### Fixes

* 🐛 Add support for an argument of type `Optional[Tuple]` and default value `None`. PR [#757](https://github.com/khulnasoft/cligenius/pull/757) by [@Asthestarsfalll](https://github.com/Asthestarsfalll).

### Docs

* 🔧 Fix typo in Github template. PR [#793](https://github.com/khulnasoft/cligenius/pull/793) by [@svlandeg](https://github.com/svlandeg).
* 📝 Fix typos in documentation. PR [#761](https://github.com/khulnasoft/cligenius/pull/761) by [@svlandeg](https://github.com/svlandeg).
* 📝 Update console output with Click 8 messages. PR [#789](https://github.com/khulnasoft/cligenius/pull/789) by [@svlandeg](https://github.com/svlandeg).
* 📝 Remove references to a .rst README generated by poetry new. PR [#632](https://github.com/khulnasoft/cligenius/pull/632) by [@jonasmmiguel](https://github.com/jonasmmiguel).

## 0.12.1

Now you don't need to install `cligenius[all]`. When you install `cligenius` it comes with the default optional dependencies and the `cligenius` command.

If you don't want the extra optional dependencies (`rich` and `shellingham`), you can install `cligenius-slim` instead.

You can also install `cligenius-slim[standard]`, which includes the default optional dependencies, but not the `cligenius` command.

Now the package `cligenius-cli` doesn't add anything on top of what `cligenius` has, it only depends on `cligenius`, and is there only for backwards compatibility, so that projects that depend on `cligenius-cli` can get the latest features of the `cligenius` command while they upgrade their dependencies to require `cligenius` directly.

### Features

* ✨ Add support for `cligenius ./someprogram.py utils docs --title`. PR [#782](https://github.com/khulnasoft/cligenius/pull/782) by [@khulnasoft](https://github.com/khulnasoft).

### Fixes

* 🐛 Fix broken installation when upgrading from `cligenius <0.12.0` to `cligenius >=0.12.0`, make `cligenius` independent of `cligenius-slim`, include `cligenius` command in `cligenius` package. PR [#791](https://github.com/khulnasoft/cligenius/pull/791) by [@khulnasoft](https://github.com/khulnasoft).

This fixes a problem that would break the `cligenius` installation directory when upgrading from `cligenius <0.12.0` to `cligenius >=0.12.0`, see issue [#790](https://github.com/khulnasoft/cligenius/issues/790).

By installing the latest version (`0.12.1`) it fixes it, for any previous version, even if the installation directory was already broken by the previous upgrade.

### Internal

* 👷 Add cron to run test once a week on monday. PR [#783](https://github.com/khulnasoft/cligenius/pull/783) by [@estebanx64](https://github.com/estebanx64).

## 0.12.0

In version `0.12.0`, the `cligenius` package depends on `cligenius-slim[standard]` which includes the default dependencies (instead of `cligenius[all]`) and `cligenius-cli` (that provides the `cligenius` command).

If you don't want the extra optional dependencies (`rich` and `shellingham`), you can install `cligenius-slim` instead.

You can also install `cligenius-slim[standard]`, which includes the default optional dependencies, but not the `cligenius` command.

In version `0.12.0` the `cligenius-cli` package only provides the `cligenius` command, but the code is still in the main code, so even without installing `cligenius-cli`, it can be called with `python -m cligenius`.

This approach of having `cligenius` depend on `cligenius-slim[standard]` instead of including the whole code and dependencies itself caused an issue when upgrading from `cligenius <0.12.0` to `cligenius >=0.12.0`, see issue [#790](https://github.com/khulnasoft/cligenius/issues/790). This is fixed in version `0.12.1`.

### Features

* ✨ Add `cligenius-slim` package without extras, make `cligenius` include `cligenius-slim[default]` and integrate Cligenius CLI (`cligenius` command) into Cligenius. PR [#780](https://github.com/khulnasoft/cligenius/pull/780) by [@khulnasoft](https://github.com/khulnasoft).

### Internal

* 🔧 Temporarily disable social plugin while a MkDocs issue is handled. PR [#779](https://github.com/khulnasoft/cligenius/pull/779) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Fix install MkDocs Insiders only when available. PR [#778](https://github.com/khulnasoft/cligenius/pull/778) by [@khulnasoft](https://github.com/khulnasoft).

## 0.11.1

### Fixes

* 🔧 Explicitly include testing files in sdist for redistributors (e.g. OpenSUSE) and add CI to test redistribution. PR [#773](https://github.com/khulnasoft/cligenius/pull/773) by [@khulnasoft](https://github.com/khulnasoft).

### Internal

* 👷 Do not use the cache for dependencies when publishing to PyPI. PR [#774](https://github.com/khulnasoft/cligenius/pull/774) by [@khulnasoft](https://github.com/khulnasoft).

## 0.11.0

### Breaking Changes

* 🔧 Refactor package manager, move from Flit to PDM, remove private pip extras for `test`, `doc`, `dev`. PR [#764](https://github.com/khulnasoft/cligenius/pull/764) by [@khulnasoft](https://github.com/khulnasoft).
* 🔥 Remove support for Click 7, require Click 8+. PR [#760](https://github.com/khulnasoft/cligenius/pull/760) by [@khulnasoft](https://github.com/khulnasoft).
* 🔥 Remove support for Python 3.6. PR [#758](https://github.com/khulnasoft/cligenius/pull/758) by [@khulnasoft](https://github.com/khulnasoft).

### Refactors

* 🔧 Migrate from Black, isort, flake8, autoflake, pyupgrade to Ruff. PR [#763](https://github.com/khulnasoft/cligenius/pull/763) by [@khulnasoft](https://github.com/khulnasoft).

### Internal

* ⬆️ Upgrade coverage and configs. PR [#769](https://github.com/khulnasoft/cligenius/pull/769) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Upgrade mypy and config. PR [#768](https://github.com/khulnasoft/cligenius/pull/768) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Upgrade Smokeshow GitHub action. PR [#767](https://github.com/khulnasoft/cligenius/pull/767) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Upgrade latest-changes GitHub Action. PR [#766](https://github.com/khulnasoft/cligenius/pull/766) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Upgrade issue-manager GitHub Action. PR [#765](https://github.com/khulnasoft/cligenius/pull/765) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Add alls-green to CI. PR [#759](https://github.com/khulnasoft/cligenius/pull/759) by [@khulnasoft](https://github.com/khulnasoft).

## 0.10.0

### Fixes

* 🐛 Fix default value of `None` for CLI Parameters when the type is `list | None` and the default value is `None`. PR [#664](https://github.com/khulnasoft/cligenius/pull/664) by [@theowisear](https://github.com/theowisear).

## 0.9.4

### Features

* ✨ Improve support for CLI translations using gettext. PR [#417](https://github.com/khulnasoft/cligenius/pull/417) by [@mjodmj](https://github.com/mjodmj).

## 0.9.3

### Fixes

* 🐛 Fix evaluating stringified annotations in Python 3.10 (also `from __future__ import annotations`). PR [#721](https://github.com/khulnasoft/cligenius/pull/721) by [@heckad](https://github.com/heckad).

## 0.9.2

### Fixes

* 🐛 Fix display of default value for Enum parameters inside of a list, include docs and tests. PR [#473](https://github.com/khulnasoft/cligenius/pull/473) by [@asieira](https://github.com/asieira).
* 🐛 Update type annotations for `show_default` parameter and update docs for setting a "Custom default string". PR [#501](https://github.com/khulnasoft/cligenius/pull/501) by [@plannigan](https://github.com/plannigan).

### Docs

* 📝 Add docs and test for `no_args_is_help` feature. PR [#751](https://github.com/khulnasoft/cligenius/pull/751) by [@svlandeg](https://github.com/svlandeg).

## 0.9.1

### Fixes

* 🐛 Add missing `default_factory` in `Argument` overloads. PR [#750](https://github.com/khulnasoft/cligenius/pull/750) by [@m9810223](https://github.com/m9810223).
* 🐛 Fix preserving case in enum values. PR [#571](https://github.com/khulnasoft/cligenius/pull/571) by [@avaldebe](https://github.com/avaldebe).

### Docs

* 📝 Remove obsolete references to `--install-completion` for `cligenius.run()` scripts. PR [#595](https://github.com/khulnasoft/cligenius/pull/595) by [@khulnasoft](https://github.com/khulnasoft).

* 📝 Update docs example for a Cligenius/Click group to make new subcommands explicit. PR [#755](https://github.com/khulnasoft/cligenius/pull/755) by [@svlandeg](https://github.com/svlandeg).
* 📝 Update docs for building a package, file structure example. PR [#683](https://github.com/khulnasoft/cligenius/pull/683) by [@davidbgk](https://github.com/davidbgk).
* 📝 Update link in docs to the newest stable version of click. PR [#675](https://github.com/khulnasoft/cligenius/pull/675) by [@javier171188](https://github.com/javier171188).
* 🔧 Add `CITATION.cff` file for academic citations. PR [#681](https://github.com/khulnasoft/cligenius/pull/681) by [@khulnasoft](https://github.com/khulnasoft).
* ✏ Fix typo in `docs/tutorial/exceptions.md`. PR [#702](https://github.com/khulnasoft/cligenius/pull/702) by [@menzenski](https://github.com/menzenski).
* ✏ Fix typo in `docs/tutorial/options/name.md`. PR [#725](https://github.com/khulnasoft/cligenius/pull/725) by [@bwagner](https://github.com/bwagner).
* ✏ Fix typo in `docs/tutorial/arguments/optional.md`. PR [#602](https://github.com/khulnasoft/cligenius/pull/602) by [@tadasgedgaudas](https://github.com/tadasgedgaudas).

### Internal

* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#606](https://github.com/khulnasoft/cligenius/pull/606) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* 👷 Install MkDocs Material Insiders only when secrets are available, for Dependabot. PR [#685](https://github.com/khulnasoft/cligenius/pull/685) by [@khulnasoft](https://github.com/khulnasoft).
* ⚒️ Update build-docs.yml, do not zip docs. PR [#645](https://github.com/khulnasoft/cligenius/pull/645) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Deploy docs to Cloudflare. PR [#644](https://github.com/khulnasoft/cligenius/pull/644) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Upgrade CI for docs. PR [#642](https://github.com/khulnasoft/cligenius/pull/642) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update token for latest changes. PR [#635](https://github.com/khulnasoft/cligenius/pull/635) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update CI workflow dispatch for latest changes. PR [#643](https://github.com/khulnasoft/cligenius/pull/643) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update token for Material for MkDocs Insiders. PR [#636](https://github.com/khulnasoft/cligenius/pull/636) by [@khulnasoft](https://github.com/khulnasoft).
* 🐛 Fix internal type annotations and bump mypy version. PR [#638](https://github.com/khulnasoft/cligenius/pull/638) by [@paulo-raca](https://github.com/paulo-raca).
* 💡 Add comments to document overload definitions in code. PR [#752](https://github.com/khulnasoft/cligenius/pull/752) by [@svlandeg](https://github.com/svlandeg).
* 🔥 Remove Jina QA Bot as it has been discontinued. PR [#749](https://github.com/khulnasoft/cligenius/pull/749) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update build docs CI cache paths. PR [#707](https://github.com/khulnasoft/cligenius/pull/707) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Upgrade latest-changes GitHub Action. PR [#691](https://github.com/khulnasoft/cligenius/pull/691) by [@khulnasoft](https://github.com/khulnasoft).

## 0.9.0

### Features

* ✨ Add support for PEP-593 `Annotated` for specifying options and arguments. Initial PR [#584](https://github.com/khulnasoft/cligenius/pull/584) by [@ryangalamb](https://github.com/ryangalamb).
    * New docs: [Optional CLI arguments](https://cligenius.khulnasoft.com/tutorial/arguments/optional/#an-alternative-cli-argument-declaration).
    * It is no longer required to pass a default value of `...` to mark a *CLI Argument* or *CLI Option* as required.
    * It is now recommended to use `Annotated` for `cligenius.Option()` and `cligenius.Argument()`.
    * All the docs have been updated to recommend `Annotated`.

### Docs

* 📝 Update docs examples for custom param types using `Annotated`, fix overloads for `cligenius.Argument`. PR [#594](https://github.com/khulnasoft/cligenius/pull/594) by [@khulnasoft](https://github.com/khulnasoft).

### Internal

* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#592](https://github.com/khulnasoft/cligenius/pull/592) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).

## 0.8.0

### Features

* ✨ Add support for custom types and parsers. Initial PR [#583](https://github.com/khulnasoft/cligenius/pull/583) by [@jpurviance](https://github.com/jpurviance). Based on original PR [#443](https://github.com/khulnasoft/cligenius/pull/443) by [@paulo-raca](https://github.com/paulo-raca).
    * New docs: [CLI Parameter Types: Custom Types](https://cligenius.khulnasoft.com/tutorial/parameter-types/custom-types/).

### Upgrades

* ⬆ Upgrade Rich, support 13.x. PR [#524](https://github.com/khulnasoft/cligenius/pull/524) by [@musicinmybrain](https://github.com/musicinmybrain).

### Docs

* 📝 Tweak docs, Custom Types path, main page and READAME colors, broken links. PR [#588](https://github.com/khulnasoft/cligenius/pull/588) by [@khulnasoft](https://github.com/khulnasoft).
* ✏ Fix spelling (shinny -> shiny). PR [#586](https://github.com/khulnasoft/cligenius/pull/586) by [@runofthemill](https://github.com/runofthemill).
* 📝 Update docs about helping Cligenius. PR [#547](https://github.com/khulnasoft/cligenius/pull/547) by [@khulnasoft](https://github.com/khulnasoft).
* ✏️ Fix typo in datetime docs. PR [#495](https://github.com/khulnasoft/cligenius/pull/495) by [@huxuan](https://github.com/huxuan).
* ✏️ Add quotes to package name that includes brackets in docs. PR [#475](https://github.com/khulnasoft/cligenius/pull/475) by [@gjolga](https://github.com/gjolga).

### Internal

* ⬆ Bump dawidd6/action-download-artifact from 2.24.2 to 2.26.0. PR [#558](https://github.com/khulnasoft/cligenius/pull/558) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#549](https://github.com/khulnasoft/cligenius/pull/549) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* 🔧 Add `exclude_lines` to coverage configuration. PR [#585](https://github.com/khulnasoft/cligenius/pull/585) by [@dmontagu](https://github.com/dmontagu).
* ⬆️ Upgrade analytics. PR [#557](https://github.com/khulnasoft/cligenius/pull/557) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Update new issue chooser to suggest GitHub Discussions. PR [#544](https://github.com/khulnasoft/cligenius/pull/544) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Add GitHub Discussion templates for questions. PR [#541](https://github.com/khulnasoft/cligenius/pull/541) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Update pre-commit, Python version, isort version. PR [#542](https://github.com/khulnasoft/cligenius/pull/542) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#512](https://github.com/khulnasoft/cligenius/pull/512) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump nwtgck/actions-netlify from 1.2.4 to 2.0.0. PR [#513](https://github.com/khulnasoft/cligenius/pull/513) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Refactor CI artifact upload/download for docs previews. PR [#516](https://github.com/khulnasoft/cligenius/pull/516) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#500](https://github.com/khulnasoft/cligenius/pull/500) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump actions/cache from 2 to 3. PR [#496](https://github.com/khulnasoft/cligenius/pull/496) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump dawidd6/action-download-artifact from 2.24.1 to 2.24.2. PR [#494](https://github.com/khulnasoft/cligenius/pull/494) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump dawidd6/action-download-artifact from 2.9.0 to 2.24.1. PR [#491](https://github.com/khulnasoft/cligenius/pull/491) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/setup-python from 2 to 4. PR [#492](https://github.com/khulnasoft/cligenius/pull/492) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷‍♂️ Consistently use `sys.executable` to run subprocesses, needed by OpenSUSE. PR [#408](https://github.com/khulnasoft/cligenius/pull/408) by [@theMarix](https://github.com/theMarix).
* 👷‍♂️ Ensure the `PYTHONPATH` is set properly when testing the tutorial scripts. PR [#407](https://github.com/khulnasoft/cligenius/pull/407) by [@theMarix](https://github.com/theMarix).

## 0.7.0

### Features

* ✨ Make `cligenius.run()` not add completion scripts by default, it only makes sense in installed apps. Also update docs for handling [autocompletion in CLI options](https://cligenius.khulnasoft.com/tutorial/options-autocompletion/). PR [#488](https://github.com/khulnasoft/cligenius/pull/488) by [@khulnasoft](https://github.com/khulnasoft).
* ✨ Add support for Python 3.11, tests in CI and official marker. PR [#487](https://github.com/khulnasoft/cligenius/pull/487) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Add CI for Python 3.10. PR [#384](https://github.com/khulnasoft/cligenius/pull/384) by [@khulnasoft](https://github.com/khulnasoft).

### Fixes

* 🎨 Fix type annotation of `cligenius.run()`. PR [#284](https://github.com/khulnasoft/cligenius/pull/284) by [@yassu](https://github.com/yassu).
* 🎨 Fix type annotations for `get_group`. PR [#430](https://github.com/khulnasoft/cligenius/pull/430) by [@khulnasoft](https://github.com/khulnasoft).

### Docs

* 📝 Add note about how subcommands with function names using underscores are converted to dashes. PR [#403](https://github.com/khulnasoft/cligenius/pull/403) by [@targhs](https://github.com/targhs).
* 📝 Fix typo in docs at `docs/tutorial/commands/help.md`. PR [#466](https://github.com/khulnasoft/cligenius/pull/466) by [@fepegar](https://github.com/fepegar).
* ✏ Fix link in docs to `datetime.strptime()`. PR [#464](https://github.com/khulnasoft/cligenius/pull/464) by [@Kobu](https://github.com/Kobu).
* ✏ Update `first-steps.md`, clarify distinction between parameter and argument. PR [#176](https://github.com/khulnasoft/cligenius/pull/176) by [@mccarthysean](https://github.com/mccarthysean).
* ✏ Fix broken plac link. PR [#275](https://github.com/khulnasoft/cligenius/pull/275) by [@mgielda](https://github.com/mgielda).

### Internal

* ✅ Add extra tests just for coverage because monkeypatching with strange imports confuses coverage. PR [#490](https://github.com/khulnasoft/cligenius/pull/490) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Tweak pytest coverage. PR [#485](https://github.com/khulnasoft/cligenius/pull/485) by [@khulnasoft](https://github.com/khulnasoft).
* ➕ Bring back pytest-cov because coverage can't detect pytest-xdist. PR [#484](https://github.com/khulnasoft/cligenius/pull/484) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ Bump actions/upload-artifact from 2 to 3. PR [#477](https://github.com/khulnasoft/cligenius/pull/477) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/checkout from 2 to 3. PR [#478](https://github.com/khulnasoft/cligenius/pull/478) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#411](https://github.com/khulnasoft/cligenius/pull/411) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump nwtgck/actions-netlify from 1.1.5 to 1.2.4. PR [#479](https://github.com/khulnasoft/cligenius/pull/479) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump khulnasoft/issue-manager from 0.2.0 to 0.4.0. PR [#481](https://github.com/khulnasoft/cligenius/pull/481) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Move from pytest-cov to coverage and Codecov to Smokeshow. PR [#483](https://github.com/khulnasoft/cligenius/pull/483) by [@khulnasoft](https://github.com/khulnasoft).
* ➕ Add extra Material for MkDocs deps for docs. PR [#482](https://github.com/khulnasoft/cligenius/pull/482) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Update Dependabot config. PR [#476](https://github.com/khulnasoft/cligenius/pull/476) by [@khulnasoft](https://github.com/khulnasoft).

## 0.6.1

### Fixes

* 🐛 Fix setting `FORCE_TERMINAL` with colors 2. PR [#424](https://github.com/khulnasoft/cligenius/pull/424) by [@khulnasoft](https://github.com/khulnasoft).
* 🐛 Fix setting `FORCE_TERMINAL` with colors. PR [#423](https://github.com/khulnasoft/cligenius/pull/423) by [@khulnasoft](https://github.com/khulnasoft).

## 0.6.0

This release adds deep integrations with [Rich](https://rich.readthedocs.io/en/stable/). ✨

`rich` is an optional dependency, you can install it directly or it will be included when you install with:

```console
$ pip install "cligenius[all]"
```

If Rich is available, it will be used to show the content from `--help` options, validation errors, and even errors in your app (exception tracebacks).

There are new options to group commands, *CLI arguments*, and *CLI options*, support for [Rich Console Markup](https://rich.readthedocs.io/en/stable/markup.html), and more! 🎉

### Features

* ✨ Richify, add integrations with Rich everywhere. PR [#419](https://github.com/khulnasoft/cligenius/pull/419) by [@khulnasoft](https://github.com/khulnasoft).
    * Recommend Rich as the main information displaying tool, new docs: [Printing and Colors](https://cligenius.khulnasoft.com/tutorial/printing/).
    * For most use cases not using Rich, use plain `print()` instead of `cligenius.echo()` in the docs, to simplify the concepts and avoid confusions. New docs: [Printing and Colors - cligenius Echo](https://cligenius.khulnasoft.com/tutorial/printing/#cligenius-echo).
    * Define help panels for *CLI arguments*, new docs: [CLI Arguments with Help - CLI Argument help panels](https://cligenius.khulnasoft.com/tutorial/arguments/help/#cli-argument-help-panels).
    * Define help panels for *CLI options*, new docs: [CLI Options with Help - CLI Options help panels](https://cligenius.khulnasoft.com/tutorial/options/help/#cli-options-help-panels).
    * New docs for deprecating commands: [Commands - Command Help - Deprecate a Command](https://cligenius.khulnasoft.com/tutorial/commands/help/#deprecate-a-command).
    * Support for Rich Markdown in docstrings, *CLI parameters* `help`, and `epilog` with the new parameter `cligenius.Cligenius(rich_markup_mode="markdown")`, new docs: [Commands - Command Help - Rich Markdown and Markup](https://cligenius.khulnasoft.com/tutorial/commands/help/#rich-markdown-and-markup).
    * Support for Rich Markup (different from Markdown) in docstrings, *CLI parameters* `help`, and `epilog` with the new parameter `cligenius.Cligenius(rich_markup_mode="rich")`, new docs: [Commands - Command Help - Rich Markdown and Markup](https://cligenius.khulnasoft.com/tutorial/commands/help/#rich-markdown-and-markup).
    * Define help panels for *commands*, new docs: [Commands - Command Help - Help Panels](https://cligenius.khulnasoft.com/tutorial/commands/help/#help-panels).
    * New docs for setting an `epilog`, with support for Rich Markdown and Console Markup, new docs: [Commands - Command Help - Epilog](https://cligenius.khulnasoft.com/tutorial/commands/help/#epilog).
* ✨ Refactor and document handling pretty exceptions. PR [#422](https://github.com/khulnasoft/cligenius/pull/422) by [@khulnasoft](https://github.com/khulnasoft).
    * Add support for customizing pretty short errors, new docs: [Exceptions and Errors](https://cligenius.khulnasoft.com/tutorial/exceptions/).
* ✨ Allow configuring pretty errors when creating the Cligenius instance. PR [#416](https://github.com/khulnasoft/cligenius/pull/416) by [@khulnasoft](https://github.com/khulnasoft).

### Docs

* 📝 Add docs for using Rich with Cligenius. PR [#421](https://github.com/khulnasoft/cligenius/pull/421) by [@khulnasoft](https://github.com/khulnasoft).
    * Add new docs: [Ask with Prompt - Prompt with Rich](https://cligenius.khulnasoft.com/tutorial/prompt/#prompt-with-rich).
    * Add new docs to handle progress bars and spinners with Rich: [Progress Par](https://cligenius.khulnasoft.com/tutorial/progressbar/).

### Internal

* ⬆️ Upgrade codecov GitHub Action. PR [#420](https://github.com/khulnasoft/cligenius/pull/420) by [@khulnasoft](https://github.com/khulnasoft).

## 0.5.0

### Features

* ✨ Add pretty error tracebacks for user errors and support for Rich. PR [#412](https://github.com/khulnasoft/cligenius/pull/412) by [@khulnasoft](https://github.com/khulnasoft).

### Docs

* ✏ Fix typo, "ASCII codes" to "ANSI escape sequences". PR [#308](https://github.com/khulnasoft/cligenius/pull/308) by [@septatrix](https://github.com/septatrix).

## 0.4.2

### Fixes

* 🐛 Fix type conversion for `List` and `Tuple` and their internal types. PR [#143](https://github.com/khulnasoft/cligenius/pull/143) by [@hellowhistler](https://github.com/hellowhistler).
* 🐛 Fix `context_settings` for a Cligenius app with a single command. PR [#210](https://github.com/khulnasoft/cligenius/pull/210) by [@daddycocoaman](https://github.com/daddycocoaman).

### Docs

* 📝 Clarify testing documentation about checking `stderr`. PR [#335](https://github.com/khulnasoft/cligenius/pull/335) by [@cgabard](https://github.com/cgabard).
* ✏ Fix typo in docs for CLI Option autocompletion. PR [#288](https://github.com/khulnasoft/cligenius/pull/288) by [@graue70](https://github.com/graue70).
* 🎨 Fix header format for "Standard Input" in `docs/tutorial/printing.md`. PR [#386](https://github.com/khulnasoft/cligenius/pull/386) by [@briancohan](https://github.com/briancohan).
* ✏ Fix typo in `docs/tutorial/terminating.md`. PR [#382](https://github.com/khulnasoft/cligenius/pull/382) by [@kianmeng](https://github.com/kianmeng).
* ✏ Fix syntax typo in `docs/tutorial/package.md`. PR [#333](https://github.com/khulnasoft/cligenius/pull/333) by [@ryanstreur](https://github.com/ryanstreur).
* ✏ Fix typo, duplicated word in `docs/tutorial/options/required.md`.. PR [#316](https://github.com/khulnasoft/cligenius/pull/316) by [@michaelriri](https://github.com/michaelriri).
* ✏ Fix minor typo in `index.md`. PR [#274](https://github.com/khulnasoft/cligenius/pull/274) by [@RmStorm](https://github.com/RmStorm).
* ✏ Fix double "and" typo in first-steps tutorial. PR [#225](https://github.com/khulnasoft/cligenius/pull/225) by [@softwarebloat](https://github.com/softwarebloat).
* 🎨 Fix format in docs explaining `datetime` parameter type. PR [#220](https://github.com/khulnasoft/cligenius/pull/220) by [@DiegoPiloni](https://github.com/DiegoPiloni).

### Internal

* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#404](https://github.com/khulnasoft/cligenius/pull/404) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* 👷 Fix Material for MkDocs install in CI. PR [#395](https://github.com/khulnasoft/cligenius/pull/395) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Add pre-commit CI config. PR [#394](https://github.com/khulnasoft/cligenius/pull/394) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Clear MkDocs Insiders cache. PR [#393](https://github.com/khulnasoft/cligenius/pull/393) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Add pre-commit config and formatting. PR [#392](https://github.com/khulnasoft/cligenius/pull/392) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Disable installing MkDocs Insiders in forks. PR [#391](https://github.com/khulnasoft/cligenius/pull/391) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆️ Upgrade Codecov GitHub Action. PR [#383](https://github.com/khulnasoft/cligenius/pull/383) by [@khulnasoft](https://github.com/khulnasoft).

## 0.4.1

### Fixes

* 🐛 Fix import of `get_terminal_size` for Click 8.1.0 support and upgrade Black to fix CI. PR [#380](https://github.com/khulnasoft/cligenius/pull/380) by [@khulnasoft](https://github.com/khulnasoft) based on original PR [#375](https://github.com/khulnasoft/cligenius/pull/375) by [@madkinsz](https://github.com/madkinsz).

### Internal

* 📝 Add Jina's QA Bot to the docs to help people that want to ask quick questions. PR [#368](https://github.com/khulnasoft/cligenius/pull/368) by [@khulnasoft](https://github.com/khulnasoft).
* 💚 Only test on push when on master, avoid duplicate CI runs from PRs. PR [#358](https://github.com/khulnasoft/cligenius/pull/358) by [@khulnasoft](https://github.com/khulnasoft).
* ✨ Add support for previewing docs in PRs from forks and enable MkDocs Insiders. PR [#357](https://github.com/khulnasoft/cligenius/pull/357) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆️ Upgrade MkDocs Material, MDX-Include, and MkDocs structure. PR [#356](https://github.com/khulnasoft/cligenius/pull/356) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update publish GitHub action. PR [#325](https://github.com/khulnasoft/cligenius/pull/325) by [@khulnasoft](https://github.com/khulnasoft).

## 0.4.0

### Features

* ✨ Add support for Click 8 while keeping compatibility with Click 7. PR [#317](https://github.com/khulnasoft/cligenius/pull/317) by [@khulnasoft](https://github.com/khulnasoft).

### Internal

* 📝 Add Security policy. PR [#324](https://github.com/khulnasoft/cligenius/pull/324) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Add updated issue templates. PR [#323](https://github.com/khulnasoft/cligenius/pull/323) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Enable tests for Python 3.9. PR [#322](https://github.com/khulnasoft/cligenius/pull/322) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Add GitHub Action Latest Changes. PR [#321](https://github.com/khulnasoft/cligenius/pull/321) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update docs CI name. PR [#320](https://github.com/khulnasoft/cligenius/pull/320) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Add sponsors docs and badge. PR [#319](https://github.com/khulnasoft/cligenius/pull/319) by [@khulnasoft](https://github.com/khulnasoft).

## 0.3.2

### Features

* Add support for `mypy --strict`. Original PR [#147](https://github.com/khulnasoft/cligenius/pull/147) by [@victorphoenix3](https://github.com/victorphoenix3).

### Docs

* Update docs with new `--help` showing default values. PR [#135](https://github.com/khulnasoft/cligenius/pull/135) by [@victorphoenix3](https://github.com/victorphoenix3).
* Add `Optional` to docs for *CLI Arguments and Options* with a default of `None`. PR [#131](https://github.com/khulnasoft/cligenius/pull/131) by [@rkbeatss](https://github.com/rkbeatss).
* Add valid date formats to docs. PR [#122](https://github.com/khulnasoft/cligenius/pull/122) by [@IamCathal](https://github.com/IamCathal).

### Internal

* Report coverage in XML to support GitHub Actions. PR [#146](https://github.com/khulnasoft/cligenius/pull/146).
* Update badges and remove Travis, now that GitHub Actions is the main CI. PR [#145](https://github.com/khulnasoft/cligenius/pull/145).

## 0.3.1

* Add GitHub Actions, move from Travis. PR [#144](https://github.com/khulnasoft/cligenius/pull/144).
* Pin dependencies. PR [#138](https://github.com/khulnasoft/cligenius/pull/138).
* Add Dependabot. PR [#136](https://github.com/khulnasoft/cligenius/pull/136).
* Upgrade Isort to version 5.x.x. PR [#137](https://github.com/khulnasoft/cligenius/pull/137).

## 0.3.0

* Add support for `help` parameter in *CLI arguments*:
    * As `help` in *CLI arguments* is not supported by Click, there are two new internal classes (Click sub-classes) to support it:
        * `cligenius.core.CligeniusArgument`
        * `cligenius.core.CligeniusCommand`
    * This includes a new auto-generated help text section `Arguments` for *CLI arguments*, showing defaults, required arguments, etc.
    * It's also possible to disable it and keep the previous behavior, not showing automatic help for *CLI arguments* (Click's default) using the `hidden` parameter.
    * Now `show_default` is `True` by default.
    * And now `show_envvar` is `True` by default.
    * So, default values and env vars are shown in the help text by default, without having to manually enable them, for both *CLI arguments* and *CLI options*.
    * New docs:
        * [CLI Arguments Intro](https://cligenius.khulnasoft.com/tutorial/arguments/).
        * [Optional CLI Arguments](https://cligenius.khulnasoft.com/tutorial/arguments/optional/).
        * [CLI Arguments with Default](https://cligenius.khulnasoft.com/tutorial/arguments/default/).
        * [CLI Arguments with Help](https://cligenius.khulnasoft.com/tutorial/arguments/help/).
        * [CLI Arguments with Environment Variables](https://cligenius.khulnasoft.com/tutorial/arguments/envvar/).
        * [CLI Arguments: Other uses](https://cligenius.khulnasoft.com/tutorial/arguments/other-uses/).
        * [CLI arguments with tuples](https://cligenius.khulnasoft.com/tutorial/multiple-values/arguments-with-multiple-values/#cli-arguments-with-tuples).
    * Lot's of tests for all the new examples in the new docs, keeping coverage at 100%.
    * PR [#123](https://github.com/khulnasoft/cligenius/pull/123).
* Add docs for calling packages with `python -m some_package` using `__main__.py`: [Building a Package: Support `python -m`](https://cligenius.khulnasoft.com/tutorial/package/#support-python-m-optional). PR [#121](https://github.com/khulnasoft/cligenius/pull/121).
* Add support for `*args` and `**kwargs` when calling the Cligenius app, just like in Click. PR [#120](https://github.com/khulnasoft/cligenius/pull/120) by [@teymour-aldridge](https://github.com/teymour-aldridge).
* Fix typos in README and main docs [#103](https://github.com/khulnasoft/cligenius/pull/103) by [@mrcartoonster](https://github.com/mrcartoonster).
* Fix typo in docs. PR [#98](https://github.com/khulnasoft/cligenius/pull/98) by [@mrcartoonster](https://github.com/mrcartoonster).
* Fix typos and rewording in docs. PR [#97](https://github.com/khulnasoft/cligenius/pull/97) by [@mrcartoonster](https://github.com/mrcartoonster).
* Update GitHub Action issue-manager. PR [#114](https://github.com/khulnasoft/cligenius/pull/114).

## 0.2.1

* Add support for forward references (types declared inside of strings). PR [#93](https://github.com/khulnasoft/cligenius/pull/93).

## 0.2.0

* Add support for completion for commands/programs not available on startup.
    * This allows installing a Cligenius program/script in a virtual environment and still have completion globally installed.
    * PR [#92](https://github.com/khulnasoft/cligenius/pull/92).
* Add note about `cligenius.echo()` and `print()` for colors in Windows. PR [#89](https://github.com/khulnasoft/cligenius/pull/89).
* Upgrade Mkdocs-Material version, update contributing guide style. PR [#90](https://github.com/khulnasoft/cligenius/pull/90).

## 0.1.1

* Fix completion evaluation for Bash and Zsh when the program is not installed/found. PR [#83](https://github.com/khulnasoft/cligenius/pull/83).
* Fix completion script for Fish. PR [#82](https://github.com/khulnasoft/cligenius/pull/82).
* Fix shell installation for Bash to `~/.bashrc` and update Windows development docs. PR [#81](https://github.com/khulnasoft/cligenius/pull/81).
* Update coverage badge. PR [#78](https://github.com/khulnasoft/cligenius/pull/78).

## 0.1.0

* Fix coverage instructions. PR [#72](https://github.com/khulnasoft/cligenius/pull/72).
* Add docs for [Building a Package](https://cligenius.khulnasoft.com/tutorial/package/). PR [#71](https://github.com/khulnasoft/cligenius/pull/71).
* Add docs for [Using Click (with Cligenius)](https://cligenius.khulnasoft.com/tutorial/using-click/). PR [#70](https://github.com/khulnasoft/cligenius/pull/70).
* Add support for type-based callbacks and autocompletion functions, extra tests and docs:
    * Extra tests, raising coverage to 100%.
    * New docs: [Printing and Colors: "Standard Output" and "Standard Error"](https://cligenius.khulnasoft.com/tutorial/printing/#standard-output-and-standard-error).
    * New docs: [Password CLI Option and Confirmation Prompt](https://cligenius.khulnasoft.com/tutorial/options/password/).
    * Support for callbacks based on type annotations. New docs: [CLI Option Callback and Context](https://cligenius.khulnasoft.com/tutorial/options/callback-and-context/).
    * New docs: [Version CLI Option, is_eager](https://cligenius.khulnasoft.com/tutorial/options/version/).
    * Support for autocompletion functions based on type annotations. New docs: [CLI Option autocompletion](https://cligenius.khulnasoft.com/tutorial/options/autocompletion/).
    * New docs: [Commands: Using the Context](https://cligenius.khulnasoft.com/tutorial/commands/context/).
    * New docs: [Testing](https://cligenius.khulnasoft.com/tutorial/testing/).
    * PR [#68](https://github.com/khulnasoft/cligenius/pull/68).
* Fix Zsh completion install script. PR [#69](https://github.com/khulnasoft/cligenius/pull/69).
* Fix typo in progressbar example. PR [#63](https://github.com/khulnasoft/cligenius/pull/63) by [@ValentinCalomme](https://github.com/ValentinCalomme).

## 0.0.11

* Re-implement completion system:
    * Remove optional dependency `click-completion` (with its sub-dependencies, like Jinja).
    * Add optional dependency `shellingham` to auto detect shell to install (it was used by `click-completion`).
    * Completion now doesn't require a third party library.
        * If `shellingham` is not installed/added as a dependency, `--install-completion` and `--show-completion` take a value with the name of the shell.
    * Fix support for user provided completion in *CLI Parameters*.
    * Fix completion for files in Bash, Zsh, and Fish.
    * Add support for modern versions of PowerShell, 5, 6, and 7 (e.g. in Windows 10).
    * Add support for `pwsh` (PowerShell Core).
        * PowerShell support includes help strings for commands and *CLI Parameters*.
    * Several bug fixes.
    * Tests for the completion logic/code.
    * Tested in all the shells in Linux and Windows.
    * PR [#66](https://github.com/khulnasoft/cligenius/pull/66).
* Fix format in docs with highlighted lines. PR [#65](https://github.com/khulnasoft/cligenius/pull/65).
* Add docs about [Cligenius CLI - completion for small scripts](https://cligenius.khulnasoft.com/cligenius-cli/). PR [#64](https://github.com/khulnasoft/cligenius/pull/64).
* Add docs about [Alternatives, Inspiration and Comparisons](https://cligenius.khulnasoft.com/alternatives/). PR [#62](https://github.com/khulnasoft/cligenius/pull/62).
* Add [Development - Contributing Guide](https://cligenius.khulnasoft.com/contributing/). PR [#61](https://github.com/khulnasoft/cligenius/pull/61).

## 0.0.10

* Add support for Click version 7.1.1. PR [#60](https://github.com/khulnasoft/cligenius/pull/60).

## 0.0.9

* Add support for PEP 561, to allow `mypy` to type check applications built with **Cligenius**. PR [#58](https://github.com/khulnasoft/cligenius/pull/58).
* Upgrade deploy docs to Netlify GitHub action. PR [#57](https://github.com/khulnasoft/cligenius/pull/57).
* Add support for Mermaid JS for visualizations. PR [#56](https://github.com/khulnasoft/cligenius/pull/56).
* Update CI to run docs deployment in GitHub actions. PR [#50](https://github.com/khulnasoft/cligenius/pull/50).
* Update format for internal links. PR [#38](https://github.com/khulnasoft/cligenius/pull/38).
* Tweak external links' format. PR [#36](https://github.com/khulnasoft/cligenius/pull/36).

## 0.0.8

* Update docs and add latest changes to MkDocs/website. PR [#33](https://github.com/khulnasoft/cligenius/pull/33).
* Add extra tests for edge cases that don't belong in docs' examples. PR [#32](https://github.com/khulnasoft/cligenius/pull/32).
* Add docs for CLI Parameters with [Multiple Values](https://cligenius.khulnasoft.com/tutorial/multiple-values/). Includes tests for all the examples and bug fixes. PR [#31](https://github.com/khulnasoft/cligenius/pull/31).
* Add docs for extra *CLI parameter* types: [CLI Parameter Types: Number](https://cligenius.khulnasoft.com/tutorial/parameter-types/number/) and [CLI Parameter Types: Boolean CLI Options](https://cligenius.khulnasoft.com/tutorial/parameter-types/bool/). PR [#30](https://github.com/khulnasoft/cligenius/pull/30).
* Extend docs for Commands, add [Commands: Cligenius Callback](https://cligenius.khulnasoft.com/tutorial/commands/callback/) and [Commands: One or Multiple](https://cligenius.khulnasoft.com/tutorial/commands/one-or-multiple/). This includes tests for all the examples and bug fixes. PR [#29](https://github.com/khulnasoft/cligenius/pull/29).
* Add docs for [SubCommands - Command Groups](https://cligenius.khulnasoft.com/tutorial/subcommands/). This includes tests for all the examples and bug fixes. PR [#28](https://github.com/khulnasoft/cligenius/pull/28).
* Remove unneeded code for argument handling. PR [#26](https://github.com/khulnasoft/cligenius/pull/26).
* Add docs for [Launching Applications](https://cligenius.khulnasoft.com/tutorial/launch/). PR [#25](https://github.com/khulnasoft/cligenius/pull/25).
* Add docs for getting the [CLI Application Directory](https://cligenius.khulnasoft.com/tutorial/app-dir/). PR [#24](https://github.com/khulnasoft/cligenius/pull/24).
* Add docs for [Progress Bars](https://cligenius.khulnasoft.com/tutorial/progressbar/). PR [#23](https://github.com/khulnasoft/cligenius/pull/23).
* Add docs for [Asking with Interactive Prompts](). PR [#22](https://github.com/khulnasoft/cligenius/pull/22).
* Update docs for path *CLI option*. PR [#21](https://github.com/khulnasoft/cligenius/pull/21).
* Add colors module and docs for [Printing and Colors](https://cligenius.khulnasoft.com/tutorial/printing/) and for [Terminating](https://cligenius.khulnasoft.com/tutorial/terminating/), including tests. PR [#20](https://github.com/khulnasoft/cligenius/pull/20).
* Refactor docs to make each individual page/section "bite-sized" / small. Add docs for [CLI option names](https://cligenius.khulnasoft.com/tutorial/options/name/). Update `cligenius.Argument()` to remove invalid positional `param_decls`. PR [#19](https://github.com/khulnasoft/cligenius/pull/19).

## 0.0.7

* Add docs for [*CLI parameter* types](https://cligenius.khulnasoft.com/tutorial/parameter-types/). Includes tests and file classes refactor. PR [#17](https://github.com/khulnasoft/cligenius/pull/17).
* Add tests for completion. PR [#15](https://github.com/khulnasoft/cligenius/pull/15) and [#16](https://github.com/khulnasoft/cligenius/pull/16).

## 0.0.6

* Add docs for [Commands](https://cligenius.khulnasoft.com/tutorial/commands/). Includes a bug fix for handling default values set in `cligenius.Cligenius()` parameters. PR [#14](https://github.com/khulnasoft/cligenius/pull/14).
* Add docs for [CLI Arguments](https://cligenius.khulnasoft.com/tutorial/arguments/). PR [#13](https://github.com/khulnasoft/cligenius/pull/13).
* Add docs for [CLI Options](https://cligenius.khulnasoft.com/tutorial/options/). PR [#12](https://github.com/khulnasoft/cligenius/pull/12).

## 0.0.5

* Clean exports from Cligenius. Remove unneeded components from Click and add needed `Exit` exception. PR [#11](https://github.com/khulnasoft/cligenius/pull/11).
* Fix and document extracting help from a function's docstring [First Steps: Document your CLI app](https://cligenius.khulnasoft.com/tutorial/first-steps/#document-your-cli-app). PR [#10](https://github.com/khulnasoft/cligenius/pull/10).
* Update references to `--install-completion` and `--show-completion` in docs. PR [#9](https://github.com/khulnasoft/cligenius/pull/9).
* Fix testing utilities, add tests for First Steps examples. PR [#8](https://github.com/khulnasoft/cligenius/pull/8).
* Add auto completion options by default when [click-completion](https://github.com/click-contrib/click-completion) is installed: `--install-completion` and `--show-completion`. PR [#7](https://github.com/khulnasoft/cligenius/pull/7).
* Update Termynal to have fixed sizes, add "fast" button, and use it in [First Steps](https://cligenius.khulnasoft.com/tutorial/first-steps/). PR [#6](https://github.com/khulnasoft/cligenius/pull/6).
* Add custom automatic [Termynal](https://github.com/khulnasoft/termynal) for docs. PR [#5](https://github.com/khulnasoft/cligenius/pull/5).

## 0.0.4

* Update short descriptions and assets.
* Docs rewording and fix typos. PR [#1](https://github.com/khulnasoft/cligenius/pull/1) by [@mariacamilagl](https://github.com/mariacamilagl).

## 0.0.3

* Fix group creation without name.

## 0.0.2

* Add initial version of code, docs, etc.

## 0.0.1

* First commit. Publish to PyPI to reserve package name.
