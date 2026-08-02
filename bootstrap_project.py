from pathlib import Path

# =====================================================
# 🐦 Angry Bird Project Bootstrap
# Version : 0.1.0 Alpha
# Purpose : Automatically generate the complete project
#           structure for Angry Bird.
# =====================================================

# -----------------------------
# Folder Structure
# -----------------------------
PROJECT_STRUCTURE = [
    # Application
    "app",
    # UI Components
    "ui/components",

    # Core Modules
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
    "core/config",

    # Shared
    "shared",

    # AI
    "ai",

    # Skills
    "skills",

    # Automation
    "automation",

    # Mobile
    "mobile",

    # User Interface
    "ui",

    # Data
    "data",
    "data/database",
    "data/knowledge",
    "data/cache",

    # Config
    "config",

    # Assets
    "assets",

    # Resources
    "resources",
    "resources/icons",
    "resources/themes",
    "resources/fonts",

    # Documentation
    "docs",

    # Tests
    "tests",

    # Scripts
    "scripts",

    # Models
    "models",

    # Logs
    "logs",
]

# -----------------------------
# Files
# -----------------------------
FILES = [

    # Root
    "main.py",
    ".env",
    ".gitignore",
    "README.md",

    # App
    "app/application.py",
    "app/bootstrap.py",
    "app/constants.py",


    # UI
    "ui/main_window.py",
    "ui/splash_screen.py",
    # UI Components
    "ui/components/top_bar.py",
    "ui/components/chat_area.py",
    "ui/components/message_bubble.py",
    "ui/components/message_input.py",
    "ui/components/status_bar.py",

    # Logger
    "core/logger/logger.py",

    # Configuration
    "core/config/config_manager.py",

    # Shared
    "shared/version.py",
    "shared/constants.py",
    "shared/helpers.py",

    # Config JSON
    "config/general.json",
    "config/ai.json",
    "config/personality.json",
    "config/voice.json",
    "config/memory.json",
    "config/security.json",
    "config/sync.json",
    "config/skills.json",
]

# -----------------------------
# Helper Function
# -----------------------------
def create_file(file_path: Path):
    """Create file if it does not exist."""
    if not file_path.exists():
        file_path.touch()
        print(f"📄 Created File : {file_path.relative_to(Path.cwd())}")
    else:
        print(f"✅ Exists       : {file_path.relative_to(Path.cwd())}")


# -----------------------------
# Main Bootstrap Function
# -----------------------------
def bootstrap():
    root = Path.cwd()

    print("\n" + "=" * 55)
    print("🐦 Angry Bird Project Bootstrap")
    print("=" * 55)

    print("\n📁 Creating folders...\n")

    for folder in PROJECT_STRUCTURE:
        folder_path = root / folder
        folder_path.mkdir(parents=True, exist_ok=True)

        init_file = folder_path / "__init__.py"

        # Don't create __init__.py inside resource folders
        if folder not in [
            "resources",
            "resources/icons",
            "resources/themes",
            "resources/fonts",
            "assets",
            "config",
            "docs",
            "logs",
            "models",
        ]:
            init_file.touch(exist_ok=True)

        print(f"📂 {folder}")

    print("\n📄 Creating files...\n")

    for file in FILES:
        create_file(root / file)

    print("\n" + "=" * 55)
    print("✅ Angry Bird Project Created Successfully!")
    print("=" * 55)


# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    bootstrap()