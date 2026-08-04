from core.automation.app_finder import AppFinder

finder = AppFinder()

apps = [
    "chrome",
    "code",
    "spotify",
    "notepad",
    "calc"
]

for app in apps:

    print(f"\nSearching for {app}")

    result = finder.find(app)

    print(result)