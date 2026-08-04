class ConversationMemory:
    """
    Stores the recent conversation between the user and Angry Bird.
    """

    def __init__(self, max_messages=10):
        self.max_messages = max_messages
        self.messages = []

    def add_user_message(self, message):
        self.messages.append({
            "role": "User",
            "content": message
        })
        self._trim()

    def add_ai_message(self, message):
        self.messages.append({
            "role": "Angry Bird",
            "content": message
        })
        self._trim()

    def get_context(self):
        """
        Returns the conversation as plain text.
        """

        context = ""

        for msg in self.messages:
            context += f"{msg['role']}: {msg['content']}\n"

        return context

    def clear(self):
        self.messages.clear()

    def _trim(self):
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]