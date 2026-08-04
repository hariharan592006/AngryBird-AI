import subprocess

from core.automation.app_finder import AppFinder


class AppLauncher:

    def __init__(self):
        self.finder = AppFinder()

    def launch(self, app_name: str):

        app_name = app_name.lower().strip()

        # -----------------------------
        # Windows Special Apps
        # -----------------------------
        special_apps = {
            "calc": "calc",
            "calculator": "calc",
            "settings": "start ms-settings:",
            "camera": "start microsoft.windows.camera:",
        }

        if app_name in special_apps:

            command = special_apps[app_name]

            if command.startswith("start "):
                subprocess.Popen(command, shell=True)
            else:
                subprocess.Popen(command)

            return f"Opening {app_name.title()}..."

        # -----------------------------
        # Normal Applications
        # -----------------------------
        executable = self.finder.find(app_name)

        if executable:

            subprocess.Popen(executable)

            return f"Opening {app_name.title()}..."

        return f"I couldn't find {app_name}."