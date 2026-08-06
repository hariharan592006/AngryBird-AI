from core.automation.command_parser import CommandParser
from core.automation.app_launcher import AppLauncher
from core.automation.web_launcher import WebLauncher


class CommandInterpreter:

    def __init__(self):

        self.parser = CommandParser()
        self.launcher = AppLauncher()
        self.web_launcher = WebLauncher()

    def execute(self, command: str):

        result = self.parser.parse(command)

        if result is None:
            return "Sorry, I couldn't understand that command."

        kind, target = result

        if kind == "app":
            return self.launcher.launch(target)

        if kind == "website":
            return self.web_launcher.launch(target)

        return "Sorry, I couldn't understand that command."