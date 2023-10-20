from functools import cache
from typing import List

from wand.image import Image

from co2data.pdf.page_provider import PageProvider


class CachingPageProvider(PageProvider):

    def __init__(self, page_provider: PageProvider):
        self._page_provider = page_provider

    @cache
    def get_page(self, file_identifier: str, page_nr: int) -> Image:
        return self._page_provider.get_page(file_identifier, page_nr)

    @cache
    def get_nr_of_pages(self, file_identifier: str) -> int:
        return self._page_provider.get_nr_of_pages(file_identifier)

    def populate_cache(self, file_identifiers: List[str]) -> None:
        for file_identifier in file_identifiers:
            nr_pages = self.get_nr_of_pages(file_identifier)
            for page in range(nr_pages):
                self.get_page(file_identifier, page)