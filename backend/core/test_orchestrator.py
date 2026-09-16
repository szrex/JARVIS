import asyncio

from core.orchestrator import orchestrator
from core.system_module import SystemModule
from llm.manager import llm_manager
from llm.ollama_provider import OllamaProvider


async def main():

    orchestrator.register_module(
        SystemModule()
    )

    llm_manager.set_provider(
        OllamaProvider(
            model="mistral:latest"
        )
    )

    orchestrator.set_llm_manager(
        llm_manager
    )

    orchestrator.start()

    response = await orchestrator.process_command(
        "What is your primary function?"
    )

    print("\nJARVIS:")
    print(response)

    print("\nSTATUS:")
    print(orchestrator.status())


if __name__ == "__main__":
    asyncio.run(main())
