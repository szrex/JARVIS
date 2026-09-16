from llm.base import LLMProvider


class MockLLMProvider(LLMProvider):

    name = "mock"

    async def generate(self, prompt: str, system_prompt: str = "") -> str:
        return f"JARVIS received: {prompt}"

    async def health_check(self) -> bool:
        return True
