from pathlib import Path
from typing import List

from . import settings
import typer
from .engine import VirusEngine
from rich import print_json
from .textwrapper import console_log, get_console


def check_file_exist(path):
    cwd = Path.cwd()
    if not (cwd / path).exists():
        raise typer.BadParameter(f"File does not exist : {path}")
    return path


def check_files_exist(paths):
    cwd = Path.cwd()

    for path in paths:
        if not (cwd / path).exists():
            raise typer.BadParameter(f"File does not exist : {path}")
    return paths


app = typer.Typer(
    name="virus",
    add_completion=False,
    help="Virus (Validation is Required for Understanding Schema)",
)


@app.command("validate")
def validate(
    src: List[str] = typer.Argument(
        ..., help="Path to the source file", callback=check_files_exist
    ),
    config_path: str = typer.Option(
        settings.DEFAULT_DATASET_RULES,
        help="Path to the config file with Dataset and rules mapping",
        callback=check_file_exist,
    ),
    is_terminal: bool = typer.Option(True, help="Output to terminal"),
    log_file_path: str = typer.Option(
        settings.DEFAULT_LOG_FILE, help="Path to the log file"
    ),
):
    console_out = get_console(is_terminal, log_file_path)
    virus = VirusEngine(config_path)
    for each_path in src:
        dataset_schema = virus._get_schema(each_path)
        if dataset_schema:
            for each_file, each_df in virus.retrieve_dataset(each_path):
                response = virus.validate_with_schema(dataset_schema, each_df)
                console_log(console_out, response, each_file)


@app.command("validate-all")
def validate_all(
    config_path: str = typer.Option(
        settings.DEFAULT_DATASET_RULES,
        help="Path to the config file with Dataset and rules mapping",
        callback=check_file_exist,
    ),
    is_terminal: bool = typer.Option(True, help="Output to terminal"),
    log_file_path: str = typer.Option(
        settings.DEFAULT_LOG_FILE, help="Path to the log file"
    ),
):
    console_out = get_console(is_terminal, log_file_path)
    virus = VirusEngine(config_path)

    for each_path in virus._get_schema_mapping():
        dataset_schema = virus._get_schema(each_path)

        if dataset_schema:
            for each_file, each_df in virus.retrieve_dataset(each_path):
                response = virus.validate_with_schema(dataset_schema, each_df)
                console_log(console_out, response, each_file)


@app.command("list")
def list_schema(
    schema_path: Path = typer.Option(
        (Path.cwd() / settings.DEFAULT_DATASET_RULES),
        help="Path to the schema file",
        callback=check_file_exist,
    )
):
    print_json(schema_path.read_text(encoding="UTF-8"))


def main():
    app()

# if __name__ == "__main__":
#     app()
