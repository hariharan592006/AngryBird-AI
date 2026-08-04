from core.ai.ai_service import AIService

ai = AIService()

print("=" * 50)
print("Angry Bird AI Service Test")
print("=" * 50)

while True:
    user = input("\nYou: ")

    if user.lower() in ["exit", "quit"]:
        break

    print("\nAngry Bird:\n")

    reply = ai.ask(user)

    print(reply)