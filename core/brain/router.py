import re


class AIRouter:

    def route(self, prompt: str):

        prompt = prompt.lower()

        # ========================
        # MEMORY
        # ========================

        if any(x in prompt for x in [
            "my name",
            "where do i study",
            "who am i",
            "my favourite"
        ]):
            return "MEMORY"

        # ========================
        # COMMAND
        # ========================

        if prompt.startswith("open "):
            return "COMMAND"

        # ========================
        # TOOL
        # ========================

        if re.search(r"\d+\s*[\+\-\*/%]\s*\d+", prompt):
            return "TOOL"

        if any(x in prompt for x in [

            "calculate",

            "time",

            "date",

            "today",

            "random",

            "password",

            "convert",

            "km",

            "kg",

            "cm",

            "hours",

            "minutes",

            "seconds",

            "miles"

        ]):
            return "TOOL"

        # ========================
        # AI
        # ========================

        return "AI"