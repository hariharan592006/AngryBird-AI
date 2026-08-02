from core.logger.logger import get_logger
from core.config.config_manager import ConfigManager


class SystemInitializer:
    """
    Responsible for initializing all core services
    before Angry Bird starts.
    """

    def __init__(self):
        self.logger = get_logger()
        self.config = ConfigManager()

    def initialize(self):
        self.logger.info("======================================")
        self.logger.info("🐦 Starting Angry Bird")
        self.logger.info("======================================")

        self.logger.info("Loading configuration...")
        general_config = self.config.load("general.json")

        self.logger.info("Configuration loaded successfully.")

        self.logger.info("System initialization completed.")

        return True