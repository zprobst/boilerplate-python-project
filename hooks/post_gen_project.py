import subprocess

# Install Dependencies and make sure everything works.
subprocess.call(['bash', './scripts/setup.sh'])
subprocess.call(['bash', './scripts/test.sh'])

# Create Git Repo and push
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-n', '-m', 'Initial commit'])
subprocess.call(['git', 'remote', 'add', 'origin', '{{ cookiecutter.project_empty_repo}}'])
subprocess.call(['git', 'push', '-u', 'origin', 'master'])