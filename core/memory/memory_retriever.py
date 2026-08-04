from core.memory.memory_classifier import MemoryClassifier


class MemoryRetriever:

    def __init__(self, memory_manager):

        self.memory = memory_manager
        self.classifier = MemoryClassifier()

    def search(self, prompt):

        # Find which memory category the prompt refers to
        memory_key = self.classifier.classify(prompt)

        if memory_key is None:
            return None, None

        # Look up the stored value
        value = self.memory.get(memory_key)

        if value is None:
            return None, None

        return memory_key, value