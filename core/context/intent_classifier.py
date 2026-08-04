class IntentClassifier:

    def classify(self, message: str) -> str:
        """
        Returns one of:

        MEMORY
        COMMAND
        TOOL
        AI
        UNKNOWN
        """

        message = message.lower()

        # -------------------------
        # Memory Questions
        # -------------------------
        memory_words = [
            "my name",
            "my favourite",
            "my favorite",
            "where do i study",
            "where do i live",
            "what is my",
            "who am i",
            "remember"
        ]

        if any(word in message for word in memory_words):
            return "MEMORY"

        # -------------------------
        # Commands
        # -------------------------
        command_words = [
            "open",
            "close",
            "shutdown",
            "restart",
            "launch"
        ]

        if any(message.startswith(cmd) for cmd in command_words):
            return "COMMAND"

        # -------------------------
        # Tool Requests
        # -------------------------
        tool_words = [
            "calculate",
            "convert",
            "translate",
            "summarize"
        ]

        if any(word in message for word in tool_words):
            return "TOOL"

        # -------------------------
        # Default
        # -------------------------
        return "AI"