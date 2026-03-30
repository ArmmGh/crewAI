"""SentenceTransformer embedding providers."""

from localagents.rag.embeddings.providers.sentence_transformer.sentence_transformer_provider import (
    SentenceTransformerProvider,
)
from localagents.rag.embeddings.providers.sentence_transformer.types import (
    SentenceTransformerProviderConfig,
    SentenceTransformerProviderSpec,
)


__all__ = [
    "SentenceTransformerProvider",
    "SentenceTransformerProviderConfig",
    "SentenceTransformerProviderSpec",
]
