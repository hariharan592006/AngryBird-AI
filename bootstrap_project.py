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

    # ===========================
    # Application
    # ===========================
    "app",

    # ===========================
    # Core
    # ===========================
    "core",

    "core/ai",
    "core/brain",
    "core/context",
    "core/personality",
    "core/memory",
    "core/automation",
    "core/command_interpreter",
    "core/tools",
    "core/web",
    "core/weather",
    "core/files",
    "core/logger",
    "core/security",
    "core/planner",
    "core/config",
    "core/sync",

    # ===========================
    # UI
    # ===========================
    "ui",
    "ui/components",

    # ===========================
    # Shared
    # ===========================
    "shared",

    # ===========================
    # AI Models
    # ===========================
    "models",

    # ===========================
    # Data
    # ===========================
    "data",
    "data/database",
    "data/cache",
    "data/knowledge",

    # ===========================
    # Assets
    # ===========================
    "assets",

    # ===========================
    # Resources
    # ===========================
    "resources",
    "resources/icons",
    "resources/themes",
    "resources/fonts",

    # ===========================
    # Config
    # ===========================
    "config",

    # ===========================
    # Docs
    # ===========================
    "docs",

    # ===========================
    # Tests
    # ===========================
    "tests",

    # ===========================
    # Scripts
    # ===========================
    "scripts",

    # ===========================
    # Logs
    # ===========================
    "logs",
]

# -----------------------------
# Files
# -----------------------------
FILES = [

    # ==================================================
    # Root
    # ==================================================
    "main.py",
    ".env",
    ".gitignore",
    "README.md",

    # ==================================================
    # App
    # ==================================================
    "app/application.py",
    "app/bootstrap.py",
    "app/constants.py",

    # ==================================================
    # AI
    # ==================================================
    "core/ai/__init__.py",
    "core/ai/ai_service.py",

    # ==================================================
    # Brain
    # ==================================================
    "core/brain/__init__.py",
    "core/brain/router.py",
    "core/brain/prompt_builder.py",

    # ==================================================
    # Memory
    # ==================================================
    "core/memory/__init__.py",
    "core/memory/conversation.py",
    "core/memory/memory_manager.py",
    "core/memory/memory_db.py",
    "core/memory/memory_extractor.py",
    "core/memory/memory_search.py",
    "core/memory/memory_response.py",

    # ==================================================
    # Personality
    # ==================================================
    "core/personality/__init__.py",
    "core/personality/personality_loader.py",
    "core/personality/system_prompt.py",

    # ==================================================
    # Context
    # ==================================================
    "core/context/__init__.py",
    "core/context/context_engine.py",

    # ==================================================
    # Automation
    # ==================================================
    "core/automation/__init__.py",
    "core/automation/aliases.py",
    "core/automation/app_finder.py",
    "core/automation/app_launcher.py",
    "core/automation/app_registry.py",
    "core/automation/command_parser.py",

    # ==================================================
    # Command Interpreter
    # ==================================================
    "core/command_interpreter/__init__.py",
    "core/command_interpreter/command_interpreter.py",

    # ==================================================
    # TOOLS (Sprint 5)
    # ==================================================
    "core/tools/__init__.py",
    "core/tools/tool_manager.py",
    "core/tools/tool_classifier.py",
    "core/tools/calculator.py",
    "core/tools/datetime_tool.py",
    "core/tools/converter.py",
    "core/tools/random_tool.py",

    # ==================================================
    # WEB (Sprint 5)
    # ==================================================
    "core/web/__init__.py",
    "core/web/search.py",

    # ==================================================
    # WEATHER (Sprint 5)
    # ==================================================
    "core/weather/__init__.py",
    "core/weather/weather.py",

    # ==================================================
    # FILES (Sprint 5)
    # ==================================================
    "core/files/__init__.py",
    "core/files/file_manager.py",

    # ==================================================
    # Logger
    # ==================================================
    "core/logger/__init__.py",
    "core/logger/logger.py",

    # ==================================================
    # Config Manager
    # ==================================================
    "core/config/__init__.py",
    "core/config/config_manager.py",

    # ==================================================
    # Shared
    # ==================================================
    "shared/__init__.py",
    "shared/constants.py",
    "shared/helpers.py",
    "shared/version.py",

    # ==================================================
    # UI
    # ==================================================
    "ui/__init__.py",
    "ui/main_window.py",
    "ui/splash_screen.py",

    "ui/components/__init__.py",
    "ui/components/chat_area.py",
    "ui/components/message_input.py",
    "ui/components/message_bubble.py",
    "ui/components/top_bar.py",
    "ui/components/status_bar.py",

    # ==================================================
    # Config Files
    # ==================================================
    "config/general.json",
    "config/ai.json",
    "config/personality.json",
    "config/memory.json",
    "config/security.json",
    "config/skills.json",
    "config/sync.json",
    "config/voice.json",

    # ==================================================
    # Tests
    # ==================================================
    "tests/test_ai_service.py",
    "tests/test_app_finder.py",
    "tests/test_app_launcher.py",
    "tests/test_command.py",
    "tests/test_context.py",
    "tests/test_router.py",
    "tests/test_memory.py",
    "tests/test_personality.py",
    "tests/test_tool_manager.py",
    "tests/test_calculator.py",
    "tests/test_datetime.py",
    "tests/test_converter.py",
    "tests/test_random.py",
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