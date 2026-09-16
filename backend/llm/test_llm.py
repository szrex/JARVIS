import asyncio

from llm.manager import llm_manager
from llm.mock_provider import MockLLMProvider


async def main():

    provider = MockLLMProvider()

    llm_manager.set_provider(provider)

    healthy = await llm_manager.health_check()

    print("LLM HEALTH:", healthy)

    response = await llm_manager.generate(
        "Hello JARVIS"
    )

    print("LLM RESPONSE:", response)


if __name__ == "__main__":
    asyncio.run(main())
