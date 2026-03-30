"""Microsoft embedding providers."""

from localagents.rag.embeddings.providers.microsoft.azure import (
    AzureProvider,
)
from localagents.rag.embeddings.providers.microsoft.types import (
    AzureProviderConfig,
    AzureProviderSpec,
)


__all__ = [
    "AzureProvider",
    "AzureProviderConfig",
    "AzureProviderSpec",
]
