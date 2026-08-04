from core.memory.memory_manager import MemoryManager
from core.context.context_engine import ContextEngine

memory = MemoryManager()

context = ContextEngine(memory)

print(context.build_context())