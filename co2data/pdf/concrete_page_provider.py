from wand.image import Image
import PyPDF2
from co2data.bills.bill_id import BillId
from co2data.pdf.page_provider import PageProvider
from co2data.pdf.pdf_store import PdfStore


class ConcretePageProvider(PageProvider):

    def __init__(self, pdf_store: PdfStore):
        self._pdf_store = pdf_store

    def get_page(self, file_identifier: str, page_nr) -> Image:
        image = self._render_all_pages(file_identifier)
        return Image(image.sequence[page_nr])

    def get_nr_of_pages(self, file_identifier: str) -> int:
        pdf_file = self._pdf_store.get(file_identifier)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        return len(pdf_reader.pages)

    def _render_all_pages(self, file_identifier) -> Image:
        filestream = self._pdf_store.get(file_identifier)
        image = Image(file=filestream, format="pdf", resolution=150)
        return image
