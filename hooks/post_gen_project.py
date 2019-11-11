import subprocess
import os

shell = os.environ.get('SHELL')

commands = [
    'poetry update',
    'poetry install',
    'git init',
    'poetry run pre-commit install',
    'poetry run pytest --cov=src tests/',
    'poetry run bandit -r src',
    'git add .',
    'git commit -n -m "Initial Commit"',
    'git remote add origin {{ cookiecutter.project_empty_repo }}',
    'git push -u origin master'
]

for command in commands:
    subprocess.call(command)
