from core.memory.memory_extractor import MemoryExtractor

extractor = MemoryExtractor()

tests = [
    "My name is Hari",
    "My favourite language is Python",
    "My favourite movie is Interstellar",
    "My favourite color is Blue",
    "I study at PSNA",
    "I live in Dindigul",
    "I work at OpenAI"
]

for test in tests:
    print("=" * 50)
    print(test)
    print(extractor.extract(test))