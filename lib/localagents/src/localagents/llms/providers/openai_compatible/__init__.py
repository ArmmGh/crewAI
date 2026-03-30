"""OpenAI-compatible providers module."""

from localagents.llms.providers.openai_compatible.completion import (
    OPENAI_COMPATIBLE_PROVIDERS,
    OpenAICompatibleCompletion,
    ProviderConfig,
)


__all__ = [
    "OPENAI_COMPATIBLE_PROVIDERS",
    "OpenAICompatibleCompletion",
    "ProviderConfig",
]
