from llm.registry import provider_registry
from llm.mock_provider import MockLLMProvider
from llm.ollama_provider import OllamaProvider


def initialize_providers():

    provider_registry.register(
        MockLLMProvider()
    )

    provider_registry.register(
        OllamaProvider(
            model="mistral:latest"
        )
    )
