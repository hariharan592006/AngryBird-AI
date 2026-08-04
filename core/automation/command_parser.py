from core.automation.app_registry import APPS


class CommandParser:

    def parse(self, prompt: str):

        prompt = prompt.lower()

        for app in APPS:

            if app in prompt:

                return app

        return None