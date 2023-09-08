from dataclasses import dataclass
from typing import List, Optional

from co2data.bills.bill_id import BillId
from co2data.categories.category import Category


@dataclass
class Position:
    """One Bill Position"""
    category: Category
    amount: float
    comment: str
    page_on_pdf: Optional[int] = None


@dataclass
class Bill:
    """Represents all climate balance relevant data for one bill"""
    id: BillId
    file_identifier: str
    positions: List[Position]

    def add_position(self, position: Position, index: int) -> None:
        """Insert position before given index."""
        self.positions.insert(index, position)

    def delete_position(self, index: int) -> None:
        """Delete position at given index."""
        self.positions.pop(index)
