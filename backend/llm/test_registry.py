from llm.providers import initialize_providers
from llm.registry import provider_registry


def main():

    initialize_providers()

    print("AVAILABLE PROVIDERS:")
    
    for provider in provider_registry.list_providers():
        print(f"- {provider}")


if __name__ == "__main__":
    main()
