import re

from core.tools.calculator import Calculator
from core.tools.datetime_tool import DateTimeTool
from core.tools.random_tool import RandomTool
from core.tools.converter import Converter
from core.tools.tool_classifier import ToolClassifier


class ToolManager:

    def __init__(self):

        self.classifier = ToolClassifier()

        self.calculator = Calculator()
        self.datetime = DateTimeTool()
        self.random = RandomTool()
        self.converter = Converter()

    def execute(self, prompt: str):

        tool = self.classifier.classify(prompt)

        # ===========================
        # Calculator
        # ===========================

        if tool == "CALCULATOR":

            expression = re.sub(
                r"(calculate|solve|evaluate)",
                "",
                prompt,
                flags=re.IGNORECASE
            ).strip()

            return self.calculator.calculate(expression)

        # ===========================
        # Date & Time
        # ===========================

        elif tool == "DATETIME":

            text = prompt.lower()

            if "time" in text:
                return self.datetime.current_time()

            if "date" in text or "today" in text:
                return self.datetime.current_date()

            if "day" in text:
                return self.datetime.current_day()

        # ===========================
        # Random
        # ===========================

        elif tool == "RANDOM":

            text = prompt.lower()

            if "password" in text:
                return self.random.random_password()

            return self.random.random_number(1, 100)

        # ===========================
        # Converter
        # ===========================

        elif tool == "CONVERTER":

            pattern = r"(\d+(?:\.\d+)?)\s+(\w+)\s+(?:to)\s+(\w+)"

            match = re.search(pattern, prompt.lower())

            if match:

                value = float(match.group(1))
                from_unit = match.group(2)
                to_unit = match.group(3)

                return self.converter.convert(
                    value,
                    from_unit,
                    to_unit
                )

            return "Invalid conversion."

        return None