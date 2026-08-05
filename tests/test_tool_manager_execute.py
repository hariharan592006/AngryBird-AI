from core.tools.tool_manager import ToolManager

tools = ToolManager()

tests = [

    "Calculate 25 * 18",

    "What time is it?",

    "Today's date",

    "Generate random password",

    "Random number",

    "Convert 5 kg to lbs",

    "Convert 10 km to miles",

]

for test in tests:

    print("User:", test)

    print("Result:", tools.execute(test))

    print("-" * 50)