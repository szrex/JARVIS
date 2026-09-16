from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """
    Standard interface for every JARVIS LLM provider.
    """

    name = "unknown"

    @abstractmethod
    async def generate(self, prompt: str, system_prompt: str = "") -> str:
        """
        Generate a response from the language model.
        """
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        """
        Check whether the provider is available.
        """
        pass
