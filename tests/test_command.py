from core.command_interpreter.command_interpreter import CommandInterpreter

cmd = CommandInterpreter()

print(cmd.execute("Open Chrome"))
print(cmd.execute("Open YouTube"))
print(cmd.execute("Open GitHub"))