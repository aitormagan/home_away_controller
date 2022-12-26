import os
import json


def get_config():
    config_file = os.environ.get("CONFIG_FILE")
    with open(config_file, "r") as f:
        config = json.load(f)
    return config
