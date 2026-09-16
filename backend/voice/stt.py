from abc import ABC, abstractmethod


class SpeechToText(ABC):

    name = "unknown"

    @abstractmethod
    async def transcribe(self, audio_data: bytes) -> str:
        """
        Convert audio data into text.
        """
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        """
        Check whether the STT engine is available.
        """
        pass
