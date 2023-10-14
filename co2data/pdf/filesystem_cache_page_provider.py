import json
import logging
import os
from functools import cache
from pathlib import Path
from typing import List, Dict

from wand.image import Image

from co2data.pdf.page_provider import PageProvider


class FileSystemCachePageProvider(PageProvider):

    def __init__(self, page_provider: PageProvider, cache_dir: Path, image_format: str = "png"):
        self._cache_dir = cache_dir
        self._page_provider = page_provider
        self._format = image_format
        self._nr_of_pages_cache_file = Path(self._cache_dir / "nr_of_pages.json")
        self._nr_of_pages_by_identifier: Dict[str, int] = {}

    @cache
    def get_page(self, file_identifier: str, page_nr: int) -> Image:
        image_file = self._create_filename(file_identifier, page_nr)
        if image_file.exists():
            return Image(filename=image_file)
        else:
            logging.warning(f"{image_file} does not exist in cache, reload from pdf.")
            return self._page_provider.get_page(file_identifier, page_nr)

    @cache
    def get_nr_of_pages(self, file_identifier: str) -> int:
        return self._page_provider.get_nr_of_pages(file_identifier)

    def _create_cache_directory_if_not_exists(self):
        if not self._cache_dir.exists():
            os.makedirs(self._cache_dir)

    def populate_cache(self, file_identifiers: List[str]) -> None:
        self._create_cache_directory_if_not_exists()
        loaded_nr_of_pages_by_identifier = self._load_nr_of_pages_cache_file()
        for file_identifier in file_identifiers:
            if file_identifier in loaded_nr_of_pages_by_identifier:
                self._nr_of_pages_by_identifier[file_identifier] = loaded_nr_of_pages_by_identifier[file_identifier]
            else:
                self._nr_of_pages_by_identifier[file_identifier] = self._page_provider.get_nr_of_pages(file_identifier)
            for page in range(self._nr_of_pages_by_identifier[file_identifier]):
                if not self._create_filename(file_identifier, page).exists():
                    page_image = self._page_provider.get_page(file_identifier, page)
                    page_image.format = "png"
                    page_image.save(filename=self._create_filename(file_identifier, page))
        with self._nr_of_pages_cache_file.open("w", encoding="utf-8") as cache_file:
            json.dump(self._nr_of_pages_by_identifier, cache_file)

    def _load_nr_of_pages_cache_file(self):
        loaded_nr_of_pages_by_identifier = {}
        if self._nr_of_pages_cache_file.exists():
            with self._nr_of_pages_cache_file.open("r", encoding="utf-8") as cache_file:
                loaded_nr_of_pages_by_identifier: Dict[str, int] = json.load(cache_file)
        return loaded_nr_of_pages_by_identifier

    def _create_filename(self, file_identifier: str, page_number: int) -> Path:
        return Path(self._cache_dir / f"{file_identifier}_{page_number}.{self._format}")
