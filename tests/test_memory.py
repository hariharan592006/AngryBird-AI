from core.memory.conversation import ConversationMemory

memory = ConversationMemory()

memory.add_user_message("Hi")
memory.add_ai_message("Hello Hari!")

memory.add_user_message("I'm learning Python.")
memory.add_ai_message("That's great!")

print(memory.get_context())