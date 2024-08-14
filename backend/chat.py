from llama_index.core import VectorStoreIndex
from llama_index.core.chat_engine.types import ChatMode

from vector_store import get_vector_store

system_prompt = "You are a helpful assistant who helps users with their questions."


def get_chat():
    vector_store = get_vector_store()
    index = VectorStoreIndex.from_vector_store(vector_store)
    return index.as_chat_engine(
        similarity_top_k=3,
        system_prompt=system_prompt,
        chat_mode=ChatMode.CONDENSE_PLUS_CONTEXT,
    )
