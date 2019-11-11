#!/bin/bash
pynev init
pyenv shell
poetry update
poetry install
poetry run pre-commit install
