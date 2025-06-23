import importlib.resources
from typing import List

from pdf2image import convert_from_path
from PIL import Image

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
        return images


def image_to_text():
    pass
