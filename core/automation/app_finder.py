from pathlib import Path

from core.automation.aliases import APP_ALIASES


class AppFinder:

    SEARCH_PATHS = [

        Path("C:/Program Files"),

        Path("C:/Program Files (x86)"),

        Path.home() / "AppData/Local/Programs",

        Path.home() / "AppData/Local/Microsoft/WindowsApps",
    ]

    def find(self, app_name: str):

        app_name = app_name.lower().strip()

        executable = APP_ALIASES.get(app_name, f"{app_name}.exe")

        candidates = []

        for folder in self.SEARCH_PATHS:

            if not folder.exists():
                continue

            try:

                for exe in folder.rglob("*.exe"):

                    filename = exe.name.lower()

                    # Ignore installers
                    if "setup" in filename:
                        continue

                    if "installer" in filename:
                        continue

                    if "uninstall" in filename:
                        continue

                    # Highest priority
                    if filename == executable:
                        return str(exe)

                    # Save similar names as fallback
                    stem = exe.stem.lower()

# Only allow safe prefix matches
                    if stem.startswith(executable.replace(".exe", "")):
                        candidates.append(str(exe))
            except Exception:
                continue

        if candidates:
            return candidates[0]

        return None