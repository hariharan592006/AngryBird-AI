from core.memory.memory_manager import MemoryManager
from core.memory.memory_search import MemorySearch

memory = MemoryManager()

search = MemorySearch(memory)

print(search.search("What is my language?"))
print(search.search("Where do I study?"))
print(search.search("What is my name?"))