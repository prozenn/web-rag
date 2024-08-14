import os

from llama_index.core.settings import Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama.base import Ollama

LLM_MODEL = "llama3.1"
EMBEDDING_MODEL = "mxbai-embed-large"
OLLAMA_BASE_URL = "http://127.0.0.1:11434"
REQUEST_TIMEOUT = 600.0

def init_ollama():
    base_url = os.getenv("OLLAMA_BASE_URL", OLLAMA_BASE_URL)

    Settings.embed_model = OllamaEmbedding(
        base_url=base_url,
        model_name=os.getenv("EMBEDDING_MODEL", EMBEDDING_MODEL),
    )

    Settings.llm = Ollama(
        base_url=base_url,
        model=os.getenv("MODEL", LLM_MODEL),
        request_timeout=REQUEST_TIMEOUT,
    )
