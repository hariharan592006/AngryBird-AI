from core.tools.random_tool import RandomTool

tool = RandomTool()

print("Random Number")
print(tool.random_number(1, 100))

print()

print("Random Choice")
print(tool.random_choice(["Apple", "Banana", "Orange"]))

print()

print("Random Password")
print(tool.random_password())