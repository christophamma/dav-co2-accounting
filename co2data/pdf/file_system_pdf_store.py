from pathlib import Path
from typing import BinaryIO, Dict

from co2data.bills.bill_id import BillId
from co2data.pdf.pdf_store import PdfStore


class FileSystemPdfStore(PdfStore):
    """
    Implements a PdfStore based on files stored in a file system.
    """

    def __init__(self):
        self.files: Dict[str, Path] = {}

    def get(self, file_identifier: str) -> BinaryIO:
        if file_identifier in self.files:
            return open(self.files[file_identifier], "br")
        else:
            raise ValueError(f"bill_id {file_identifier} not present in store")

    def add_file(self, file_identifier: str, file_path: Path) -> None:
        if file_identifier in self.files:
            raise ValueError(f"bill id {file_identifier} is already present")
        else:
            self.files[file_identifier] = file_path
