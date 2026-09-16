from core.logger import logger


class JarvisOrchestrator:

    def __init__(self):
        self.running = False
        self.modules = {}
        self.llm_manager = None

    def register_module(self, module):
        self.modules[module.name] = module
        module.initialize()

        logger.info(f"Module registered: {module.name}")

    def set_llm_manager(self, llm_manager):
        self.llm_manager = llm_manager
        logger.info("LLM manager connected.")

    async def process_command(self, command: str) -> str:

        if not self.running:
            raise RuntimeError("JARVIS is not running.")

        if self.llm_manager is None:
            raise RuntimeError("No LLM manager configured.")

        logger.info(f"Processing command: {command}")

        response = await self.llm_manager.generate(
            prompt=command,
            system_prompt=(
                "You are JARVIS, a local personal AI assistant. "
                "Be concise, accurate, and helpful."
            )
        )

        return response

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
            },
            "llm_connected": self.llm_manager is not None
        }


orchestrator = JarvisOrchestrator()
