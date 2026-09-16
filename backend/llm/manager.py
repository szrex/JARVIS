from llm.base import LLMProvider


class LLMManager:

    def __init__(self):
        self.provider: LLMProvider | None = None

    def set_provider(self, provider: LLMProvider):
        self.provider = provider

    async def generate(self, prompt: str, system_prompt: str = "") -> str:

        if self.provider is None:
            raise RuntimeError("No LLM provider configured.")

        return await self.provider.generate(
            prompt,
            system_prompt
        )

    async def health_check(self) -> bool:

        if self.provider is None:
            return False

        return await self.provider.health_check()


llm_manager = LLMManager()
