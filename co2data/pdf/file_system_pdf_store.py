from pathlib import Path
from typing import BinaryIO, Dict, List

from co2data.bills.bill_id import BillId
from co2data.pdf.pdf_store import PdfStore


class FileSystemPdfStore(PdfStore):
    """
    Implements a PdfStore based on files stored in a file system.
    """

    def __init__(self):
        self.files: Dict[str, Path] = {}

    @property
    def identifiers(self) -> List[str]:
        return list(self.files.keys())

    def has(self, file_identifier: str) -> bool:
        return file_identifier in self.files

    def get(self, file_identifier: str) -> BinaryIO:
        if file_identifier in self.files:
            return open(self.files[file_identifier], "br")
        else:
            raise ValueError(f"file with identifier {file_identifier} not present in store")

    def add_file(self, file_identifier: str, file_path: Path) -> str:
        if file_identifier in self.files:
            raise ValueError(f"file with identifier {file_identifier} is already present")
        else:
            self.files[file_identifier] = file_path
