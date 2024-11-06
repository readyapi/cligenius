#!/usr/bin/env bash

set -e
set -x

mypy cligenius
ruff check cligenius tests docs_src scripts
ruff format cligenius tests docs_src scripts --check
