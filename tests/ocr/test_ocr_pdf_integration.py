import pytest
from PIL import Image

from ves_ie_tools.constants import pdf_file_name_bphs_w_en_vol1 as pdf_file_name
from ves_ie_tools.ocr.ocr_pdf import pdf_to_image


def test_pdf_to_image_real_pdf():
    images = pdf_to_image(pdf_file_name=pdf_file_name, first_page=12, last_page=12)

    assert isinstance(images, list), "Should return a list"
    assert len(images) == 1, "Expected exactly one page image"

    image = images[0]
    assert isinstance(image, Image.Image), "List items must be PIL Images"

    width, height = image.size
    assert width > 0 and height > 0, "Image dimensions must be positive"
