# {{ cookiecutter.project_slug }}

{{ cookiecutter.prject_description }}

## Setup
To setup you need to have `pyenv` and `poetry` installed your machine and accessible in you
shell's path. Make sure pyenv has version `3.7.x` installed and run `scripts/setup.sh`.

That will setup all of the dependencies with the latet versions. After doing so, run `scripts/test.sh`, make sure all of the unit tests pass and coverage is reported. If so, then you are good and can modify the `pyproject.toml` with the right information and install more dependencies.

If you created the repository from the cookie cutter, this is done automatically for you.
