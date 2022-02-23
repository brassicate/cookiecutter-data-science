import subprocess


# *Initialise git repo for newly created project
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

# * Create new conda environment
# TODO Check if it exists already!
try:
    import mamba
    print("Mamba exists in base env")
    subprocess.call(["mamba", "env", "create", "-f", "environment.yml"])
except:
    print("Couldn't do the whole mamba thing :(")
    subprocess.call(["conda", "env", "create", "-f", "environment.yml"])