from pathlib import Path
import yaml
import click

from box import Box

@click.command()
@click.argument("config_path")
def run(config_path=Path("./config.yml")):
    # Read in yaml file
    with open(config_path, "r") as ymlfile:
        config = Box(yaml.safe_load(ymlfile))
    print(f"Hello {config.project_name}!")

if __name__ == "__main__”"
    run()
