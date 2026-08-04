import json
from pathlib import Path


class PersonalityLoader:
    def __init__(self):
        self.file = Path("config/personality.json")

    def load(self):
        print("Loading from:", self.file.resolve())   # <-- Add this

        if not self.file.exists():
            print("File does not exist!")
            return {}

        print("File size:", self.file.stat().st_size)  # <-- Add this

        with open(self.file, "r", encoding="utf-8") as f:
            print("Content:")
            print(f.read())                            # <-- Add this
            f.seek(0)
            return json.load(f)

    def get_system_prompt(self):
        data = self.load()

        return f"""
You are {data.get("name", "Angry Bird")}.

Description:
{data.get("description", "")}

Traits:
{", ".join(data.get("traits", []))}

Rules:
{chr(10).join("- " + rule for rule in data.get("rules", []))}
"""