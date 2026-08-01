from pathlib import Path

PROJECT_STRUCTURE = [
    "app",
    "core",
    "core/brain",
    "core/planner",
    "core/context",
    "core/personality",
    "core/memory",
    "core/command_interpreter",
    "core/security",
    "core/sync",
    "core/logger",
    "ai",
    "skills",
    "automation",
    "mobile",
    "ui",
    "data",
    "data/database",
    "data/knowledge",
    "data/cache",
    "config",
    "assets",
    "docs",
    "tests",
    "scripts",
    "models",
    "logs",
]

CONFIG_FILES = [
    "config/general.json",
    "config/ai.json",
    "config/personality.json",
    "config/voice.json",
    "config/memory.json",
    "config/security.json",
    "config/sync.json",
    "config/skills.json",
]

ROOT_FILES = [
    "main.py",
    ".env",
    "README.md",
]


def create_structure():
    root = Path.cwd()

    print("\n🐦 Creating Angry Bird project...\n")

    for folder in PROJECT_STRUCTURE:
        path = root / folder
        path.mkdir(parents=True, exist_ok=True)

        init = path / "__init__.py"
        init.touch(exist_ok=True)

        print(f"📁 {folder}")

    for file in CONFIG_FILES + ROOT_FILES:
        path = root / file
        path.touch(exist_ok=True)

        print(f"📄 {file}")

    print("\n✅ Project structure created successfully!")


if __name__ == "__main__":
    create_structure()