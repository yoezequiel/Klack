import os
import json

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "sound_name": "CherryMX",
    "sound_path": os.path.join("sounds", "cherrymx.mp3"),
    "volume": 0.5,
}


def load_config():
    if not os.path.exists(CONFIG_FILE):
        return DEFAULT_CONFIG

    with open(CONFIG_FILE, "r") as file:
        config = json.load(file)
        return config


def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)
