from voice.stt import SpeechToText
from voice.tts import TextToSpeech


class VoiceManager:

    def __init__(self):
        self.stt: SpeechToText | None = None
        self.tts: TextToSpeech | None = None

    def set_stt(self, provider: SpeechToText):
        self.stt = provider

    def set_tts(self, provider: TextToSpeech):
        self.tts = provider

    async def transcribe(self, audio_data: bytes) -> str:

        if self.stt is None:
            raise RuntimeError(
                "No speech-to-text provider configured."
            )

        return await self.stt.transcribe(audio_data)

    async def synthesize(self, text: str) -> bytes:

        if self.tts is None:
            raise RuntimeError(
                "No text-to-speech provider configured."
            )

        return await self.tts.synthesize(text)

    async def health_check(self):

        return {
            "stt": (
                await self.stt.health_check()
                if self.stt else False
            ),
            "tts": (
                await self.tts.health_check()
                if self.tts else False
            )
        }


voice_manager = VoiceManager()
