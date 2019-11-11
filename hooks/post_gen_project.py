import subprocess

# Install Pipenv Dependencies
subprocess.call(['poetry', 'install'])

# Create Git Repo and push
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-n', '-m', 'Initial commit'])
subprocess.call(['git', 'remote', 'add', 'origin', '{{ cookiecutter.project_empty_repo}}'])
subprocess.call(['git', 'push', '-u', 'origin', 'master'])