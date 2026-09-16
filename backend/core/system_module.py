from core.module import JarvisModule
from core.logger import logger


class SystemModule(JarvisModule):

    name = "system"

    def initialize(self):
        logger.info("System module initialized.")

    def shutdown(self):
        logger.info("System module shut down.")

    def status(self):
        return {
            "name": self.name,
            "status": "online"
        }
