import json
from pathlib import Path


class ConfigManager:

    def __init__(self):
        self.config_path = Path("config")

    def load(self, filename):
        path = self.config_path / filename

        if not path.exists():
            return {}

        with open(path, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}