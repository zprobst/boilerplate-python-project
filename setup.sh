#!/bin/bash
pyenv local
poetry update
poetry install
poetry run pre-commit install
