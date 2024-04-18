#!/usr/bin/env bash

set -e
set -x

mypy types
ruff check types tests docs_src
ruff format types tests docs_src --check
