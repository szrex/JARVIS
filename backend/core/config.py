from pathlib import Path
from dotenv import load_dotenv
import os


BASE_DIR = Path(__file__).resolve().parents[2]

ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)


class Settings:

    APP_NAME = os.getenv("APP_NAME", "JARVIS")
    APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "mock")
    LLM_MODEL = os.getenv("LLM_MODEL", "")

    VOICE_ENABLED = os.getenv("VOICE_ENABLED", "true").lower() == "true"

    MEMORY_ENABLED = os.getenv("MEMORY_ENABLED", "true").lower() == "true"

    AUTOMATION_ENABLED = os.getenv(
        "AUTOMATION_ENABLED",
        "true"
    ).lower() == "true"


settings = Settings()
