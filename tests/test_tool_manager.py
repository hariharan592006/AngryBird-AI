from core.tools.tool_manager import ToolManager

tools = ToolManager()

print("Calculator")
print(tools.calculator.calculate("25*18"))

print()

print("Time")
print(tools.datetime.current_time())

print()

print("Random")
print(tools.random.random_number(1, 100))

print()

print("Converter")
print(tools.converter.convert(5, "kg", "lbs"))