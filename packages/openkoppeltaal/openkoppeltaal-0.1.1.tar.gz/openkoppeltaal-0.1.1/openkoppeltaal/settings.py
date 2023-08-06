from pathlib import Path
from typing import Any, Union

import toml
from pydantic import BaseModel


class CommandLineArgs(BaseModel):
    # Base config
    config: str = "okpt.toml"
    debug: bool = False


class ConfigFile(CommandLineArgs):
    port: int
    fhir_version: str


def load_settings(file_path: str) -> Union[Any, dict[str, Any]]:
    path = Path(file_path)
    if path.is_file():
        with open("okpt.toml", "r") as config_file:
            return toml.loads(config_file.read())


def merge_config(config, custom_args) -> ConfigFile:
    # Merge commandline args with presedent over toml file args, except if there None
    filtered_args = {k: v for k, v in custom_args.items() if v is not None}
    return ConfigFile(**{**config, **filtered_args})
