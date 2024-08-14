import os

from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient


def get_vector_store():
    client = QdrantClient(os.getenv("QDRANT_URL", "http://localhost:6333"))

    return QdrantVectorStore(
        collection_name=os.getenv("QDRANT_COLLECTION", "default"),
        client=client,
    )
