class MemoryResponse:

    def generate(self, prompt, key, value):

        prompt = prompt.lower()

        # -----------------------------
        # User is ASKING about memory
        # -----------------------------
        question_words = [
            "what",
            "where",
            "who",
            "which",
            "tell me",
            "do you remember",
            "can you remember",
        ]

        is_question = any(word in prompt for word in question_words)

        if is_question:

            if key == "name":
                return f"Your name is {value}."

            elif key == "college":
                return f"You study at {value}."

            elif key == "language":
                return f"Your favourite language is {value}."

            else:
                return f"I remember that {key} is {value}."

        # -----------------------------
        # User is TELLING something
        # -----------------------------
        else:

            if key == "name":
                return f"Nice to meet you, {value}! I'll remember your name."

            elif key == "college":
                return f"Got it! I'll remember that you study at {value}."

            elif key == "language":
                return f"Awesome! I'll remember that your favourite language is {value}."

            else:
                return f"Got it! I'll remember that your {key} is {value}."