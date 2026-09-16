from core.logger import logger


class JarvisOrchestrator:

    def __init__(self):
        self.running = False
        self.modules = {}

    def register_module(self, module):
        """Register and initialize a JARVIS module."""
        self.modules[module.name] = module
        module.initialize()

        logger.info(f"Module registered: {module.name}")

    def start(self):
        self.running = True
        logger.info("JARVIS orchestrator started.")

    def stop(self):
        for module in self.modules.values():
            module.shutdown()

        self.running = False
        logger.info("JARVIS orchestrator stopped.")

    def status(self):
        return {
            "running": self.running,
            "modules": {
                name: module.status()
                for name, module in self.modules.items()
            }
        }


orchestrator = JarvisOrchestrator()
