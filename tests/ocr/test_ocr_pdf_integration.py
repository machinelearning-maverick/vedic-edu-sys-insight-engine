import importlib.resources
import pytest
import importlib
from PIL import Image

from ves_ie_tools.constants import resources_path
from ves_ie_tools.constants import pdf_file_name_bphs_w_en_vol1 as pdf_file_name
from ves_ie_tools.constants import png_file_name_bphs_w_en_vol1_page12 as png_file_name
from ves_ie_tools.ocr.ocr_pdf import pdf_to_image, image_to_text


def test_pdf_to_image_real_pdf():
    images = pdf_to_image(pdf_file_name=pdf_file_name, first_page=12, last_page=12)

    assert isinstance(images, list), "Should return a list"
    assert len(images) == 1, "Expected exactly one page image"

    image = images[0]
    assert isinstance(image, Image.Image), "List items must be PIL Images"

    width, height = image.size
    assert width > 0 and height > 0, "Image dimensions must be positive"


def test_image_to_text_empty_list():
    assert image_to_text([]) == ""


def test_image_to_text_real_png():
    resource = importlib.resources.files(resources_path).joinpath(png_file_name)
    with importlib.resources.as_file(resource) as image_path:
        image = Image.open(image_path)

        text = image_to_text([image])

    assert text != ""


def test_full_ocr_pdf():
    images = pdf_to_image(pdf_file_name=pdf_file_name, first_page=12, last_page=12)
    text = image_to_text(images)
    print(f"#### PDF image OCR to TEXT: {text}")

    assert text != ""
