from abc import ABC, abstractmethod


class TextToSpeech(ABC):

    name = "unknown"

    @abstractmethod
    async def synthesize(self, text: str) -> bytes:
        """
        Convert text into audio.
        """
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        """
        Check whether the TTS engine is available.
        """
        pass
