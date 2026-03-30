"""OpenCLIP embedding providers."""

from localagents.rag.embeddings.providers.openclip.openclip_provider import (
    OpenCLIPProvider,
)
from localagents.rag.embeddings.providers.openclip.types import (
    OpenCLIPProviderConfig,
    OpenCLIPProviderSpec,
)


__all__ = [
    "OpenCLIPProvider",
    "OpenCLIPProviderConfig",
    "OpenCLIPProviderSpec",
]
