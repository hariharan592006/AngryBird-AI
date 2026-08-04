from core.automation.app_launcher import AppLauncher

launcher = AppLauncher()

tests = [
    "chrome",
    "code",
    "spotify",
    "notepad",
    "calc"
]

for app in tests:

    print(launcher.launch(app))