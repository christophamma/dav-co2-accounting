# render a number of pdf files to images
import logging
from pathlib import Path
from typing import List

import typer

from co2data.pdf.concrete_page_provider import ConcretePageProvider
from co2data.pdf.file_system_pdf_store import FileSystemPdfStore
from co2data.pdf.filesystem_cache_page_provider import FileSystemCachePageProvider
from co2data.pdf.pre_render_page_provider import CachingPageProvider


def cli() -> None:
    typer.run(main)


def main(directory: Path, output_dir: Path) -> None:
    pdf_files = list(directory.glob("*.pdf"))
    logging.info(f"found {len(pdf_files)} pdf files in directory")
    render_pdf_files(pdf_files, output_dir)


def render_pdf_files(pdf_files: List[Path], output_dir):
    file_system_pdf_store = FileSystemPdfStore()
    for pdf_file in pdf_files:
        file_system_pdf_store.add_file(pdf_file.name, pdf_file)
    cache_page_provider = FileSystemCachePageProvider(CachingPageProvider(ConcretePageProvider(file_system_pdf_store)), output_dir)
    cache_page_provider.populate_cache(file_system_pdf_store.identifiers)

if __name__ == "__main__":
    cli()