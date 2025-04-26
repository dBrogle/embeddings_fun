import json
import os
from typing import Dict, List

from openai import OpenAI

from .constants import OPENAI_LARGE_EMBEDDINGS_SAVE_PATH

# Initialize the embeddings cache
_embeddings_cache: Dict[str, List[float]] = {}

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=openai_api_key)


def _load_embeddings() -> None:
    """Load embeddings from the save file if it exists."""
    global _embeddings_cache
    if os.path.exists(OPENAI_LARGE_EMBEDDINGS_SAVE_PATH):
        with open(OPENAI_LARGE_EMBEDDINGS_SAVE_PATH, "r") as f:
            _embeddings_cache = json.load(f)


def _save_embeddings() -> None:
    """Save the current embeddings cache to file."""
    os.makedirs(os.path.dirname(OPENAI_LARGE_EMBEDDINGS_SAVE_PATH), exist_ok=True)
    with open(OPENAI_LARGE_EMBEDDINGS_SAVE_PATH, "w") as f:
        json.dump(_embeddings_cache, f)


def get_embedding(text: str, model: str = "text-embedding-ada-002") -> List[float]:
    """
    Get embedding for the given text, using cache if available.

    Args:
        text: The text to get embedding for
        model: The OpenAI model to use for embeddings

    Returns:
        List[float]: The embedding vector
    """
    global _embeddings_cache

    # Load embeddings if cache is empty
    if not _embeddings_cache:
        _load_embeddings()

    # Return cached embedding if available
    if text in _embeddings_cache:
        return _embeddings_cache[text]

    response = openai_client.embeddings.create(
        input=text, model="text-embedding-3-large"
    )
    print(f"Not using cache: {text}")
    embedding = response.data[0].embedding

    # Cache and save the new embedding
    _embeddings_cache[text] = embedding
    _save_embeddings()

    return embedding
