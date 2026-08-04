from core.brain.router import AIRouter

router = AIRouter()

tests = [
    "MEMORY",
    "COMMAND",
    "TOOL",
    "AI",
    "UNKNOWN"
]

for t in tests:
    print(f"{t} -> {router.route(t)}")