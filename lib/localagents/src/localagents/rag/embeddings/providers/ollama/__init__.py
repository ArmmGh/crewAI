"""Ollama embedding providers."""

from localagents.rag.embeddings.providers.ollama.ollama_provider import (
    OllamaProvider,
)
from localagents.rag.embeddings.providers.ollama.types import (
    OllamaProviderConfig,
    OllamaProviderSpec,
)


__all__ = [
    "OllamaProvider",
    "OllamaProviderConfig",
    "OllamaProviderSpec",
]
