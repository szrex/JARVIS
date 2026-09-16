from voice.stt import SpeechToText
from voice.tts import TextToSpeech


class MockSTT(SpeechToText):

    name = "mock_stt"

    async def transcribe(self, audio_data: bytes) -> str:
        return "Hello JARVIS"

    async def health_check(self) -> bool:
        return True


class MockTTS(TextToSpeech):

    name = "mock_tts"

    async def synthesize(self, text: str) -> bytes:
        return text.encode("utf-8")

    async def health_check(self) -> bool:
        return True
