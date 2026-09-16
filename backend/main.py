from core.config import APP_NAME, APP_VERSION
from core.logger import logger
from core.orchestrator import orchestrator
from core.system_module import SystemModule


def start_jarvis():

    logger.info(f"{APP_NAME} v{APP_VERSION} starting...")

    orchestrator.register_module(SystemModule())

    orchestrator.start()

    logger.info("JARVIS core initialized.")
    logger.info(f"System status: {orchestrator.status()}")


if __name__ == "__main__":
    start_jarvis()
