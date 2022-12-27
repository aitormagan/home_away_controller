import os
import json
from exceptions import InvalidConfigurationFileError


def get_config():
    config_file = os.environ.get("CONFIG_FILE", None)

    if not config_file:
        raise InvalidConfigurationFileError("Environment variable CONFIG_FILE not set")

    try:
        with open(config_file, "r") as f:
            config = json.load(f)
        return config
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        raise InvalidConfigurationFileError(f"Config file {config_file} cannot be read or parsed")
