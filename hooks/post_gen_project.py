import subprocess


# *Initialise git repo for newly created project
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

# * Create new conda environment
# TODO Check if it exists already!
subprocess.call(["conda", "env", "create", "-f", "environment.yml"])