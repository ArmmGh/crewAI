"""Cohere embedding providers."""

from localagents.rag.embeddings.providers.cohere.cohere_provider import CohereProvider
from localagents.rag.embeddings.providers.cohere.types import (
    CohereProviderConfig,
    CohereProviderSpec,
)


__all__ = [
    "CohereProvider",
    "CohereProviderConfig",
    "CohereProviderSpec",
]
