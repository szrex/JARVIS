from llm.registry import provider_registry
from llm.mock_provider import MockLLMProvider


def initialize_providers():

    provider_registry.register(
        MockLLMProvider()
    )
