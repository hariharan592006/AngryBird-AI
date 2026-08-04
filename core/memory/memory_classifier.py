from core.memory.memory_types import MEMORY_TYPES


class MemoryClassifier:

    def classify(self, prompt: str):

        prompt = prompt.lower()

        for memory_key, keywords in MEMORY_TYPES.items():

            for keyword in keywords:

                if keyword.lower() in prompt:
                    return memory_key

        return None