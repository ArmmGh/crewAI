"""Jina embedding providers."""

from localagents.rag.embeddings.providers.jina.jina_provider import JinaProvider
from localagents.rag.embeddings.providers.jina.types import (
    JinaProviderConfig,
    JinaProviderSpec,
)


__all__ = [
    "JinaProvider",
    "JinaProviderConfig",
    "JinaProviderSpec",
]
