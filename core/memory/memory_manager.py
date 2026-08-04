from data.database.memory_db import MemoryDatabase


class MemoryManager:

    def __init__(self):
        self.db = MemoryDatabase()
        self.memory = self.db.load()

    def remember(self, key, value):
        """
        Store or update a memory.
        """
        self.memory[key] = value
        self.db.save(self.memory)

    def recall(self, key):
        """
        Retrieve one memory.
        """
        return self.memory.get(key)

    def all_memories(self):
        """
        Return all stored memories.
        """
        return self.memory

    # ----------------------------------
    # Backward compatibility
    # ----------------------------------

    def add(self, key, value):
        self.remember(key, value)

    def get(self, key):
        return self.recall(key)

    def get_all(self):
        return self.all_memories()