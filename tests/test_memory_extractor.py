from core.memory.memory_extractor import MemoryExtractor

extractor = MemoryExtractor()

tests = [
    "My name is Hari",
    "My favourite language is Python",
    "I study at PSNA",
]

for sentence in tests:
    print(sentence)
    print(extractor.extract(sentence))
    print("-" * 40)