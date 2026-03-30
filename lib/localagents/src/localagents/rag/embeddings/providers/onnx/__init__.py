"""ONNX embedding providers."""

from localagents.rag.embeddings.providers.onnx.onnx_provider import ONNXProvider
from localagents.rag.embeddings.providers.onnx.types import (
    ONNXProviderConfig,
    ONNXProviderSpec,
)


__all__ = [
    "ONNXProvider",
    "ONNXProviderConfig",
    "ONNXProviderSpec",
]
