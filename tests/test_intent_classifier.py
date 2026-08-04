from core.context.intent_classifier import IntentClassifier

classifier = IntentClassifier()

tests = [
    "What is my name?",
    "Where do I study?",
    "Open Chrome",
    "Calculate 25 * 8",
    "Who is Elon Musk?",
]

for text in tests:
    print(text)
    print("->", classifier.classify(text))
    print()