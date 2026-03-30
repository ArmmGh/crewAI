"""AWS embedding providers."""

from localagents.rag.embeddings.providers.aws.bedrock import BedrockProvider
from localagents.rag.embeddings.providers.aws.types import (
    BedrockProviderConfig,
    BedrockProviderSpec,
)


__all__ = [
    "BedrockProvider",
    "BedrockProviderConfig",
    "BedrockProviderSpec",
]
