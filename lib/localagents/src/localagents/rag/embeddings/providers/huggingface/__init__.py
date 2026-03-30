"""HuggingFace embedding providers."""

from localagents.rag.embeddings.providers.huggingface.huggingface_provider import (
    HuggingFaceProvider,
)
from localagents.rag.embeddings.providers.huggingface.types import (
    HuggingFaceProviderConfig,
    HuggingFaceProviderSpec,
)


__all__ = [
    "HuggingFaceProvider",
    "HuggingFaceProviderConfig",
    "HuggingFaceProviderSpec",
]
