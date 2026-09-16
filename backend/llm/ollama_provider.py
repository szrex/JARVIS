import httpx

from llm.base import LLMProvider


class OllamaProvider(LLMProvider):

    name = "ollama"

    def __init__(
        self,
        model: str = "mistral:latest",
        base_url: str = "http://127.0.0.1:11434"
    ):
        self.model = model
        self.base_url = base_url.rstrip("/")

    async def generate(
        self,
        prompt: str,
        system_prompt: str = ""
    ) -> str:

        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system_prompt,
            "stream": False
        }

        async with httpx.AsyncClient() as client:

            response = await client.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            return data.get("response", "")

    async def health_check(self) -> bool:

        try:

            async with httpx.AsyncClient() as client:

                response = await client.get(
                    f"{self.base_url}/api/tags",
                    timeout=5
                )

                return response.status_code == 200

        except httpx.HTTPError:

            return False
