import logging
from functools import cache

from wand.image import Image
from wand.color import Color
import PyPDF2
from co2data.bills.bill_id import BillId
from co2data.pdf.helpers import get_nr_of_pages_imagemagick, get_nr_of_pages_pypdf2
from co2data.pdf.page_provider import PageProvider
from co2data.pdf.pdf_store import PdfStore


class ConcretePageProvider(PageProvider):

    def __init__(self, pdf_store: PdfStore):
        self._pdf_store = pdf_store

    def get_page(self, file_identifier: str, page_nr) -> Image:
        image = self._render_all_pages(file_identifier)
        logging.info(f"loaded pdf with {len(image.sequence)} pages and return page {page_nr}")
        return Image(image.sequence[page_nr])

    def get_nr_of_pages(self, file_identifier: str) -> int:
        with self._pdf_store.get(file_identifier) as pdf_file:
            return get_nr_of_pages_imagemagick(pdf_file)

    def _render_all_pages(self, file_identifier) -> Image:
        with self._pdf_store.get(file_identifier) as filestream:
            img = Image(file=filestream,
                         format="pdf",
                         resolution=150,
                         background=Color("white"))
            img.alpha_channel = "background"
            return img