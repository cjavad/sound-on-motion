#!/bin/sh

# Check if pipenv is installed
if ! [ -x "$(command -v pipenv)" ]; then
  echo 'Error: pipenv is not installed.' >&2
  exit 1
fi

exec $(which pipenv) run "$@"
