from core.config import APP_NAME, APP_VERSION
from core.logger import logger


def start_jarvis():
    logger.info(f"{APP_NAME} v{APP_VERSION} starting...")
    logger.info("JARVIS core initialized.")


if __name__ == "__main__":
    start_jarvis()
