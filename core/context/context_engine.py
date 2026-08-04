class ContextEngine:

    def __init__(self, memory_manager):
        self.memory = memory_manager

    def build_context(self):

        memories = self.memory.all_memories()

        if not memories:
            return "No stored memories."

        return "\n".join(
            f"{k.title()}: {v}"
            for k, v in memories.items()
        )