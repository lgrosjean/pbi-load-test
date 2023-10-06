"""
Functions to create a JSON file ready to used by HTML
"""

import typing as t

import yaml
from loguru import logger

DEFAULT_CONFIG_PATH = "./config.yaml"


# TODO: use pydantic to load config and validate schema
def load_config(config_path: t.Optional[str] = None):
    if config_path is None:
        config_path = DEFAULT_CONFIG_PATH

    with open(config_path, "r", encoding="utf8") as config_file:
        config = yaml.safe_load(config_file)

    logger.info(f"Config loaded from {config_path}")

    return config
