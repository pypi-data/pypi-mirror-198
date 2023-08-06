import subprocess
import tomllib
import warnings
from pathlib import Path

import click


def is_config_valid(data):
    NECESSARY_FORMAT = {"help": "str", "cmd": "str", "deps": [], "outs": []}
    try:
        for s in data.values():
            if not all([i in s.keys() for i in NECESSARY_FORMAT.keys()]):
                return False
            for k, v in s.items():
                if not isinstance(v, type(NECESSARY_FORMAT[k])):
                    return False
        return True
    except Exception as e:
        print(f"config not valid, key error {e}")
        return False


def load_config():
    file_path = Path().cwd() / "kewr_config.toml"
    try:
        with file_path.open(mode="rb") as file:
            data = tomllib.load(file)
        assert is_config_valid(data), "config format validation error"
        return data
    except FileNotFoundError as e:
        print(e)
    except AssertionError as e:
        print(e)


def check_dependencies(stage_data):
    return all([Path(d).exists() for d in stage_data["deps"]])


def check_outputs(stage_data):
    return all([Path(d).exists() for d in stage_data["outs"]])


def _run(cmd):
    subprocess.run(cmd, check=True)


@click.group()
def cli():
    """A simple python script runner"""
    pass


EXAMPLE = """[stage1]
help = "description of what the stage does"
cmd = "python ex.py"
deps = []
outs = []

[stage2]
help = "description of what the stage does"
cmd = "python scripts/example.py"
deps = []
outs = []"""


def run_stage(name, data, force):
    click.echo(f"Running stage {name}")
    if (not check_outputs(data)) or force:
        assert check_dependencies(data), "Missing dependencies!"
        command = data["cmd"].split()
        _run(command)
        assert check_outputs(data), "Missing outputs!"
        click.echo(f"Stage {name} completed successfully")
    else:
        click.echo(f"All stage outputs present, skipping stage {name}")


@cli.command()
def create():
    """Create a new config"""
    out_path = Path().cwd() / "kewr_config.toml"
    if out_path.exists():
        warnings.warn("config file already exists in this location", UserWarning)
    else:
        with open(out_path, "w") as file:
            file.write(EXAMPLE)
        click.echo("Created new config")


@cli.command()
def list():
    """List stages"""
    stages = load_config()
    for k, v in stages.items():
        click.echo(f"{k} : {v['help']}")


@cli.command()
@click.argument("stage", type=str, nargs=-1)
@click.option("--force", is_flag=True, help="force running of each stage")
def run(stage, force):
    """Run specified STAGE, or list of stages, or all stages with 'all'

    python -m kewr run stage_1         #runs stage_1 only

    python -m kewr run stage_1 stage_2 #runs stage_1 then stage_2

    python -m kewr run all             #runs all stages
    """
    stages = load_config()
    all_stage_names = [i for i in stages.keys()]
    allowed_stages = all_stage_names + ["all"]
    false_stages = [s for s in stage if s not in allowed_stages]
    assert (
        not false_stages
    ), f"{false_stages} not a recognized stage, available stages are: {', '.join(allowed_stages)}"
    if "all" in stage:
        print("sdf")
        stages_to_run = all_stage_names
    else:
        stages_to_run = stage
    for k, v in stages.items():
        if k in stages_to_run:
            run_stage(k, v, force)


if __name__ == "__main__":
    cli()
