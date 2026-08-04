class MemorySearch:

    ALIASES = {

        "name": [
            "name",
            "who am i",
        ],

        "college": [
            "college",
            "study",
            "school",
            "university",
            "campus",
        ],

        "language": [
            "language",
            "coding language",
            "favourite language",
            "favorite language",
        ],

    }

    def __init__(self, memory_manager):
        self.memory = memory_manager

    def search(self, question: str):

        question = question.lower()

        memories = self.memory.all_memories()

        for key, aliases in self.ALIASES.items():

            for word in aliases:

                if word in question:

                    if key in memories:
                        return key, memories[key]

        return None, None