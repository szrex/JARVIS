import asyncio

from voice.manager import voice_manager
from voice.mock import MockSTT, MockTTS


async def main():

    voice_manager.set_stt(
        MockSTT()
    )

    voice_manager.set_tts(
        MockTTS()
    )

    status = await voice_manager.health_check()

    print("VOICE STATUS:")
    print(status)

    text = await voice_manager.transcribe(
        b"test audio"
    )

    print("\nTRANSCRIPTION:")
    print(text)

    audio = await voice_manager.synthesize(
        "JARVIS voice system operational."
    )

    print("\nTTS OUTPUT:")
    print(audio)


if __name__ == "__main__":
    asyncio.run(main())
