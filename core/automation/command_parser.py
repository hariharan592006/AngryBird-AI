from core.automation.app_registry import APPS
from core.automation.websites import WEBSITES


class CommandParser:

    VERBS = [
        "open",
        "launch",
        "start",
        "run"
    ]

    def parse(self, prompt: str):

        prompt = prompt.lower()

        if not any(v in prompt for v in self.VERBS):
            return None

        # Applications
        for app in APPS:
            if app in prompt:
                return ("app", app)

        # Websites
        for site in WEBSITES:
            if site in prompt:
                return ("website", site)

        return None