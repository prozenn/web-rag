from llama_index.core import Settings
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter

from loader import get_web_documents
from settings import init_ollama
from vector_store import get_vector_store


urls = [
]


def generate_data():
    documents = get_web_documents(urls)
    vector_store = get_vector_store()

    vector_store.clear()

    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=1024, chunk_overlap=20),
            Settings.embed_model,
        ],
        vector_store=vector_store,
    )

    pipeline.run(show_progress=True, documents=documents)


if __name__ == "__main__":
    init_ollama()
    generate_data()
