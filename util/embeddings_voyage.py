import time
import voyageai
import os
import json
from PIL import Image
from typing import Dict, List
from .constants import (
    ImageOptions,
    get_image_option_as_pil_image,
    VOYAGE_EMBEDDINGS_SAVE_PATH,
    IMAGE_OPTIONS_TEXTS,
    get_key_from_image_option,
)

voyageai.api_key = os.getenv("VOYAGE_API_KEY")
vo = voyageai.Client()

# Initialize the embeddings cache
_embeddings_cache: Dict[str, List[float]] = {}


def _load_embeddings() -> None:
    """Load embeddings from the save file if it exists."""
    global _embeddings_cache
    if os.path.exists(VOYAGE_EMBEDDINGS_SAVE_PATH):
        with open(VOYAGE_EMBEDDINGS_SAVE_PATH, "r") as f:
            _embeddings_cache = json.load(f)


def _save_embeddings() -> None:
    """Save the current embeddings cache to file."""
    os.makedirs(os.path.dirname(VOYAGE_EMBEDDINGS_SAVE_PATH), exist_ok=True)
    with open(VOYAGE_EMBEDDINGS_SAVE_PATH, "w") as f:
        json.dump(_embeddings_cache, f)


def get_embedding_for_pil_image(pil_image: Image.Image):
    # Note: PIL images can't be cached directly since they're not hashable
    # This function remains uncached
    inputs = [[pil_image]]
    return vo.multimodal_embed(
        inputs,
        model="voyage-multimodal-3",
    )


def get_embedding_for_image_option(option: ImageOptions):
    """
    Get embedding for the given image option, using cache if available.

    Args:
        option: The ImageOption to get embedding for

    Returns:
        List[float]: The embedding vector
    """
    global _embeddings_cache

    # Load embeddings if cache is empty
    if not _embeddings_cache:
        _load_embeddings()

    cache_key = get_key_from_image_option(option)

    # Return cached embedding if available
    if cache_key in _embeddings_cache:
        print("Using cache for image embedding")
        return _embeddings_cache[cache_key]

    # Get new embedding
    print("Not using cache for image embedding")
    result = get_embedding_for_pil_image(get_image_option_as_pil_image(option))
    embedding = result.embeddings[0]  # Get first embedding from result

    # Cache and save the new embedding
    _embeddings_cache[cache_key] = embedding
    _save_embeddings()

    return embedding


def get_embedding_for_text(text: str):
    """
    Get embedding for the given text, using cache if available.

    Args:
        text: The text to get embedding for

    Returns:
        List[float]: The embedding vector
    """
    global _embeddings_cache

    # Load embeddings if cache is empty
    if not _embeddings_cache:
        _load_embeddings()

    cache_key = text

    # Return cached embedding if available
    if cache_key in _embeddings_cache:
        print("Using cache for text embedding")
        return _embeddings_cache[cache_key]

    # Get new embedding
    print("Not using cache for text embedding")
    inputs = [[text]]
    result = vo.multimodal_embed(
        inputs,
        model="voyage-multimodal-3",
    )
    print("Text Result Embeddings: ", result.embeddings)
    embedding = result.embeddings[0]  # Get first embedding from result

    # Cache and save the new embedding
    _embeddings_cache[cache_key] = embedding
    _save_embeddings()

    return embedding


def test_embeddings_voyage():
    counter = 0
    for option in ImageOptions:
        print(f"Testing {option.value}")
        embedding = get_embedding_for_image_option(option)
        counter += 1
        if counter % 3 == 0:
            print("Sleeping for 60 seconds for rate limiting")
            time.sleep(60)

    text = "Hello, world!"
    embedding = get_embedding_for_text(text)
    print(embedding)


def get_embeddings_for_all_image_option_texts():
    counter = 0
    for key, value in IMAGE_OPTIONS_TEXTS.items():
        for item in value.values():
            embedding = get_embedding_for_text(item)
            print("Got embedding for ", item)
            counter += 1
            if counter % 3 == 0:
                print("Sleeping for 60 seconds for rate limiting")
                time.sleep(60)


if __name__ == "__main__":
    test_embeddings_voyage()
