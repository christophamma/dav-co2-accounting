from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from co2data.bills.bill import Bill
from co2data.bills.bill_id import BillId


class BillStore(ABC):
    """
    Provides access to bill instances.
    """

    @abstractmethod
    def get(self, bill_id: BillId) -> Bill:
        """Return bill for given bill_id."""

    @abstractmethod
    def all(self) -> List[BillId]:
        """Return list of all stored bill ids."""

    @abstractmethod
    def add(self, file_identifier: str):
        """Add a bill by providing the file identifier."""