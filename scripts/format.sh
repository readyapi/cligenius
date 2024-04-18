#!/bin/sh -e
set -x
set -e

ruff check types tests docs_src scripts --fix
ruff format types tests docs_src scripts
