from core.memory.memory_manager import MemoryManager

memory = MemoryManager()

memory.remember("name", "Hari")
memory.remember("language", "Python")
memory.remember("college", "PSNA")

print(memory.recall("name"))
print(memory.recall("language"))
print(memory.recall("college"))

print(memory.all_memories())