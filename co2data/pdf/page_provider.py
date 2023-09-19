from abc import ABC, abstractmethod

from wand.image import Image

from co2data.bills.bill_id import BillId


class PageProvider(ABC):
    """Provide access to rendered images of the pdf by page."""

    @abstractmethod
    def get_page(self, file_identifier: str, page_nr) -> Image:
        """
        Return rendered image of given page of pdf file.
        """

    @abstractmethod
    def get_nr_of_pages(self, file_identifier: str) -> int:
        """
        Return the number of pages of given pdf file.
        """