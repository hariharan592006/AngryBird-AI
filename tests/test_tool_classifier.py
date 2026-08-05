from core.tools.tool_classifier import ToolClassifier

classifier = ToolClassifier()

tests = [

    "25 * 18",

    "Calculate 100+20",

    "What time is it?",

    "Today's date",

    "Generate random password",

    "Random number",

    "Convert 10 km to miles",

    "Convert 5 kg to lbs",

    "Who is Elon Musk?"
]

for test in tests:

    print(test)

    print("->", classifier.classify(test))

    print("-" * 40)