from core.system.initializer import SystemInitializer


class Bootstrap:

    def __init__(self):
        self.initializer = SystemInitializer()

    def start(self):
        return self.initializer.initialize()