from dataclasses import dataclass
from typing import List, Optional

from dataclass_wizard import JSONWizard

from co2data.bills.bill_id import BillId
from co2data.bills.bill_status import BillStatus
from co2data.categories.category import Category


@dataclass
class Position(JSONWizard):
    """One Bill Position"""
    category: Category
    department: str
    value: float
    amount: float
    price: float
    page_on_pdf: int
    included_tax: float = 0.0


@dataclass
class Bill(JSONWizard):
    """Represents all climate balance relevant data for one bill"""
    id: BillId
    file_identifier: str
    positions: List[Position]
    status: BillStatus
    comment: str

    def add_position(self, position: Position, index: int) -> None:
        """Insert position before given index."""
        self.positions.insert(index, position)

    def delete_position(self, index: int) -> None:
        """Delete position at given index."""
        self.positions.pop(index)
