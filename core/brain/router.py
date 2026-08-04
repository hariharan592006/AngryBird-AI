class AIRouter:

    def route(self, prompt: str):

        prompt = prompt.lower()

        # ===== MEMORY =====
        if any(x in prompt for x in [
            "my name",
            "where do i study",
            "what is my favourite",
            "what's my",
            "who am i"
        ]):
            return "MEMORY"

        # ===== COMMAND =====
        if prompt.startswith("open ") or prompt.startswith("launch "):
            return "COMMAND"

        # ===== TOOL =====
        if any(x in prompt for x in [
            "calculate",
            "solve",
            "convert"
        ]):
            return "TOOL"

        # ===== AI =====
        return "AI"