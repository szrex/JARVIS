import asyncio

from llm.ollama_provider import OllamaProvider


async def main():

    provider = OllamaProvider(
        model="mistral:latest"
    )

    print("Checking Ollama...")

    healthy = await provider.health_check()

    print("OLLAMA:", "ONLINE" if healthy else "OFFLINE")

    if not healthy:
        return

    print("\nSending request...\n")

    response = await provider.generate(
        "Introduce yourself as JARVIS in one short sentence."
    )

    print("JARVIS:", response)


if __name__ == "__main__":
    asyncio.run(main())
