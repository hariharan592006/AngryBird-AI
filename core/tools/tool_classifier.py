import re


class ToolClassifier:

    def classify(self, prompt: str):

        prompt = prompt.lower().strip()

        # =========================
        # Calculator
        # =========================

        if re.search(r"\d+\s*[\+\-\*/%]\s*\d+", prompt):
            return "CALCULATOR"

        if any(word in prompt for word in [
            "calculate",
            "solve",
            "evaluate"
        ]):
            return "CALCULATOR"

        # =========================
        # Date & Time
        # =========================

        if any(word in prompt for word in [
            "time",
            "date",
            "day",
            "today"
        ]):
            return "DATETIME"

        # =========================
        # Random
        # =========================

        if any(word in prompt for word in [
            "random",
            "password",
            "otp",
            "dice",
            "coin"
        ]):
            return "RANDOM"

        # =========================
        # Converter
        # =========================

        if any(word in prompt for word in [
            "convert",
            "km",
            "kg",
            "cm",
            "miles",
            "minutes",
            "seconds",
            "hours"
        ]):
            return "CONVERTER"

        return None