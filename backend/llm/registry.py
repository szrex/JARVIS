from llm.base import LLMProvider


class ProviderRegistry:

    def __init__(self):
        self._providers: dict[str, LLMProvider] = {}

    def register(self, provider: LLMProvider):
        self._providers[provider.name] = provider

    def get(self, name: str) -> LLMProvider:
        if name not in self._providers:
            raise ValueError(
                f"LLM provider '{name}' is not registered."
            )

        return self._providers[name]

    def list_providers(self) -> list[str]:
        return list(self._providers.keys())


provider_registry = ProviderRegistry()
