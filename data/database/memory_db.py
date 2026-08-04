import json
from pathlib import Path


class MemoryDatabase:

    def __init__(self):

        self.file = Path("data/database/memory.json")

        self.file.parent.mkdir(parents=True, exist_ok=True)

        if not self.file.exists():
            self.file.write_text("{}")

    def load(self):

        try:
            with open(self.file, "r", encoding="utf-8") as f:
                return json.load(f)

        except (json.JSONDecodeError, FileNotFoundError):

            data = {}

            self.save(data)

            return data

    def save(self, memory):

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(memory, f, indent=4)