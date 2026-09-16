from core.logger import logger


class JarvisOrchestrator:
    """
    Central coordinator for JARVIS.

    The orchestrator does not directly execute tools.
    It coordinates modules and delegates actions through
    controlled interfaces.
    """

    def __init__(self):
        self.running = False
        self.modules = {}

    def register_module(self, name, module):
        """Register a JARVIS module."""
        self.modules[name] = module
        logger.info(f"Module registered: {name}")

    def start(self):
        """Start the JARVIS runtime."""
        self.running = True
        logger.info("JARVIS orchestrator started.")

    def stop(self):
        """Stop the JARVIS runtime."""
        self.running = False
        logger.info("JARVIS orchestrator stopped.")

    def status(self):
        """Return the current JARVIS runtime status."""
        return {
            "running": self.running,
            "modules": list(self.modules.keys())
        }


orchestrator = JarvisOrchestrator()
