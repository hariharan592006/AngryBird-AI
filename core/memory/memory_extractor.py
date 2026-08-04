import re

from core.memory.memory_types import MEMORY_TYPES


class MemoryExtractor:

    def extract(self, prompt):

        prompt = prompt.strip()

        lower = prompt.lower()

        memories = {}

        # ----------------------------------------
        # Generic "my xxx is yyy"
        # ----------------------------------------
        match = re.search(r"my (.+?) is (.+)", lower)

        if match:

            subject = match.group(1).strip()
            value = prompt[match.end(1) + 4:].strip(" .!?")

            for memory_key, aliases in MEMORY_TYPES.items():

                if subject == memory_key:
                    memories[memory_key] = value
                    return memories

                if subject in aliases:
                    memories[memory_key] = value
                    return memories

        # ----------------------------------------
        # Generic "I study at ..."
        # ----------------------------------------
        match = re.search(r"i study at (.+)", lower)

        if match:
            value = prompt[match.start(1):].strip(" .!?")
            memories["college"] = value
            return memories

        # ----------------------------------------
        # Generic "I work at ..."
        # ----------------------------------------
        match = re.search(r"i work at (.+)", lower)

        if match:
            value = prompt[match.start(1):].strip(" .!?")
            memories["company"] = value
            return memories

        # ----------------------------------------
        # Generic "I live in ..."
        # ----------------------------------------
        match = re.search(r"i live in (.+)", lower)

        if match:
            value = prompt[match.start(1):].strip(" .!?")
            memories["city"] = value
            return memories

        return memories