from core.config import APP_NAME, APP_VERSION
from core.logger import logger
from core.orchestrator import orchestrator
from core.system_module import SystemModule
from core.event_test import run_event_test


def start_jarvis():

    logger.info(f"{APP_NAME} v{APP_VERSION} starting...")

    orchestrator.register_module(SystemModule())

    orchestrator.start()

    run_event_test()

    logger.info("JARVIS core initialized.")
    logger.info(f"System status: {orchestrator.status()}")


if __name__ == "__main__":
    start_jarvis()
