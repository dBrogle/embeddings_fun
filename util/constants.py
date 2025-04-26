import os
from enum import Enum
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
# Paths
OPENAI_LARGE_EMBEDDINGS_SAVE_PATH = os.path.join(DATA_DIR, "openai_embeddings.json")
OPENAI_LARGE_EMBEDDINGS_SAVE_PATH = os.path.join(
    DATA_DIR, "openai_large_embeddings.json"
)
VOYAGE_EMBEDDINGS_SAVE_PATH = os.path.join(DATA_DIR, "voyage_embeddings.json")

SHP_PATH = os.path.join(BASE_DIR, "shp")


# Filenames for the images
class ImageOptions(Enum):
    BARDIRO_CROCODILO = "bardiro_crocodilo"
    BONECA_AMVALA = "boneca_amvala"
    BRARR_PATTA_PIM = "brarr_patta_pim"
    CAPUCCINO_ASASHINO = "capuccino_asashino"
    JUDGMENT_JEANNI_BANANI = "judgment_jeanni_banani"
    LA_VACA_SATURNO_SATURNITA = "la_vaca_saturno_saturnita"
    LIRILY_LARILA = "lirily_larila"
    PROSELO_CARMELO = "proselo_carmelo"
    SPRING_BEANIE_GUINI = "spring_beanie_guini"
    TRALALA = "tralala"
    TRIPY_TROPHY = "tripy_trophy"
    TUNGGUK = "tungguk"


IMAGE_OPTIONS_TEXTS_KEYS = ["italian", "english_translation", "english_description"]

IMAGE_OPTIONS_TEXTS = {
    ImageOptions.BARDIRO_CROCODILO: {
        "italian": "Bardiro Crocodilo",
        "english_translation": "Bomber Crocodile",
        "english_description": "A crocodile bomber plane in the sky",
    },
    ImageOptions.BONECA_AMVALA: {
        "italian": "Boneca Amvala",
        "english_translation": "Beloved Doll",
        "english_description": "A tire with a frog head and human legs in a town street",
    },
    ImageOptions.BRARR_PATTA_PIM: {
        "italian": "Brarr Patta Pim",
        "english_translation": "Brr Brr Bang",
        "english_description": "Tree with the head of a cozu monkey and human feet in a clearing in the forest",
    },
    ImageOptions.CAPUCCINO_ASASHINO: {
        "italian": "Capuccino Asashino",
        "english_translation": "Cappuccino Assassin",
        "english_description": "A cappuccino with a ninja headband and two swords in a dojo at night",
    },
    ImageOptions.JUDGMENT_JEANNI_BANANI: {
        "italian": "Judgment Jeanni Banani",
        "english_translation": "Judge Jeanni Banana",
        "english_description": "A banana with a chimpanzee head in the forest",
    },
    ImageOptions.LA_VACA_SATURNO_SATURNITA: {
        "italian": "La Vaca Saturno Saturnita",
        "english_translation": "The Saturn Cow",
        "english_description": "Saturn with a cow's head and human feet in a crowded city",
    },
    ImageOptions.LIRILY_LARILA: {
        "italian": "Lirily Larila",
        "english_translation": "Lyrical Larila",
        "english_description": "An elephant with the body texture of a cactus and birkenstoks in the desert",
    },
    ImageOptions.PROSELO_CARMELO: {
        "italian": "Proselo Carmelo",
        "english_translation": "Prose Caramel",
        "english_description": "A fridge with the head of a camel and brown shoes",
    },
    ImageOptions.SPRING_BEANIE_GUINI: {
        "italian": "Spring Beanie Guini",
        "english_translation": "Spring Beanie Guinea",
        "english_description": "A goose fighter jet in the sky",
    },
    ImageOptions.TRALALA: {
        "italian": "Tralala",
        "english_translation": "Tralala",
        "english_description": "A shark on the beach wearing blue nike shoes",
    },
    ImageOptions.TRIPY_TROPHY: {
        "italian": "Tripy Trophy",
        "english_translation": "Trippy Trophy",
        "english_description": "A shrimp underwater with the face of a cat",
    },
    ImageOptions.TUNGGUK: {
        "italian": "Tungguk",
        "english_translation": "Tungguk",
        "english_description": "A log with a baseball bat at a train station at night",
    },
}

IMAGE_KEY_SUFFIX = "_IMG"


def get_key_from_image_option(option: ImageOptions):
    return f"{option.value}{IMAGE_KEY_SUFFIX}"


def get_image_option_as_pil_image(option: ImageOptions):
    path = os.path.join(IMAGES_DIR, f"{option.value}.webp")
    return Image.open(path)


class ShapeFiles(Enum):
    WORLD = os.path.join(SHP_PATH, "world.shp")
    # US they have online
    US_STATES = "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json"
