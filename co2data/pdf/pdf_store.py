from abc import ABC, abstractmethod
from pathlib import Path
from typing import BinaryIO

from co2data.bills.bill_id import BillId


class PdfStore(ABC):
    """Provides access to the pdf files"""

    @abstractmethod
    def has(self, file_identifier: str) -> bool:
        """Return true if file identifier exists, false otherwise."""

    @abstractmethod
    def get(self, file_identifier: str) -> BinaryIO:
        """Return pdf as binary io stream"""

    @abstractmethod
    def add_file(self, file_identifier: str, file_path: Path) -> None:
        """Add pdf file to the store"""