from typing import BinaryIO

import PyPDF2
from wand.image import Image


def get_nr_of_pages_imagemagick(pdf_data: BinaryIO) -> int:
    img = Image(file=pdf_data, format="pdf")
    return len(img.sequence)


def get_nr_of_pages_pypdf2(pdf_data: BinaryIO) -> int:
    pdf_reader = PyPDF2.PdfReader(pdf_data)
    return len(pdf_reader.pages)
