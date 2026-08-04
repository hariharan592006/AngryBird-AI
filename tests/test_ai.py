from core.ai.ai_service import AIService

ai = AIService()

question = input("You: ")

reply = ai.ask(question)

print("\nAngry Bird:\n")
print(reply)