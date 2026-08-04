from core.memory.memory_manager import MemoryManager

memory = MemoryManager()

memory.add("name", "Hari")
memory.add("college", "PSNA")
memory.add("language", "Python")

print(memory.get_all())