from core.automation.command_parser import CommandParser
from core.automation.app_launcher import AppLauncher


class CommandInterpreter:

    def __init__(self):

        self.parser = CommandParser()
        self.launcher = AppLauncher()

    def execute(self, command: str):

        command = command.lower().strip()

        if command.startswith("open "):

            app = command.replace("open ", "", 1).strip()

            return self.launcher.launch(app)

        return "Sorry, I don't understand that command."