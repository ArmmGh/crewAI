"""Type definitions for the embeddings module."""

from typing import Any, Literal, TypeAlias

from localagents.rag.core.base_embeddings_provider import BaseEmbeddingsProvider
from localagents.rag.embeddings.providers.aws.types import BedrockProviderSpec
from localagents.rag.embeddings.providers.cohere.types import CohereProviderSpec
from localagents.rag.embeddings.providers.custom.types import CustomProviderSpec
from localagents.rag.embeddings.providers.google.types import (
    GenerativeAiProviderSpec,
    VertexAIProviderSpec,
)
from localagents.rag.embeddings.providers.huggingface.types import HuggingFaceProviderSpec
from localagents.rag.embeddings.providers.ibm.types import (
    WatsonXProviderSpec,
)
from localagents.rag.embeddings.providers.instructor.types import InstructorProviderSpec
from localagents.rag.embeddings.providers.jina.types import JinaProviderSpec
from localagents.rag.embeddings.providers.microsoft.types import AzureProviderSpec
from localagents.rag.embeddings.providers.ollama.types import OllamaProviderSpec
from localagents.rag.embeddings.providers.onnx.types import ONNXProviderSpec
from localagents.rag.embeddings.providers.openai.types import OpenAIProviderSpec
from localagents.rag.embeddings.providers.openclip.types import OpenCLIPProviderSpec
from localagents.rag.embeddings.providers.roboflow.types import RoboflowProviderSpec
from localagents.rag.embeddings.providers.sentence_transformer.types import (
    SentenceTransformerProviderSpec,
)
from localagents.rag.embeddings.providers.text2vec.types import Text2VecProviderSpec
from localagents.rag.embeddings.providers.voyageai.types import VoyageAIProviderSpec


ProviderSpec: TypeAlias = (
    AzureProviderSpec
    | BedrockProviderSpec
    | CohereProviderSpec
    | CustomProviderSpec
    | GenerativeAiProviderSpec
    | HuggingFaceProviderSpec
    | InstructorProviderSpec
    | JinaProviderSpec
    | OllamaProviderSpec
    | ONNXProviderSpec
    | OpenAIProviderSpec
    | OpenCLIPProviderSpec
    | RoboflowProviderSpec
    | SentenceTransformerProviderSpec
    | Text2VecProviderSpec
    | VertexAIProviderSpec
    | VoyageAIProviderSpec
    | WatsonXProviderSpec
)

AllowedEmbeddingProviders = Literal[
    "azure",
    "amazon-bedrock",
    "cohere",
    "custom",
    "google-generativeai",
    "google-vertex",
    "huggingface",
    "instructor",
    "jina",
    "ollama",
    "onnx",
    "openai",
    "openclip",
    "roboflow",
    "sentence-transformer",
    "text2vec",
    "voyageai",
    "watsonx",
]

EmbedderConfig: TypeAlias = (
    ProviderSpec | BaseEmbeddingsProvider[Any] | type[BaseEmbeddingsProvider[Any]]
)
