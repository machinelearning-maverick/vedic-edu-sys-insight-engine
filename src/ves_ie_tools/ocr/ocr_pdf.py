import importlib.resources
from typing import List

import pytesseract
from PIL import Image
from pdf2image import convert_from_path

from ves_ie_tools.constants import resources_path


def pdf_to_image(
    pdf_file_name: str,
    first_page: int = 1,
    last_page: int = None,
    dpi: int = 300,
    fmt: str = "png",
) -> List[Image.Image]:
    resource = importlib.resources.files(resources_path).joinpath(pdf_file_name)
    with importlib.resources.as_file(resource) as pdf_path:
        images = convert_from_path(
            str(pdf_path),
            dpi=dpi,
            first_page=first_page,
            last_page=last_page,
            fmt=fmt,
        )
        # FIXME: return - add some structure with info about processed document
        return images


def image_to_text(
    images: List[Image.Image], lang: str = "san", config: str = "--psm 6"
) -> str:
    text: str = ""
    for image in images:
        text += pytesseract.image_to_string(
            image=image,
            lang=lang,
            config=config
        )
    # FIXME: return - add some structure with info about processed document
    return text
