from typing import List

from co2data.bills.bill import Position
from co2data.bills.bill_id import BillId
from co2data.bills.bill_store import BillStore


class BillDataProvider:
    """Primary class to interact with when using and altering bill data."""

    def __init__(self, bill_store: BillStore) -> None:
        self._bill_store = bill_store

    @property
    def bill_ids(self) -> List[BillId]:
        return self._bill_store.all()

    def get_file_identifier(self, bill_id: BillId) -> str:
        return self._bill_store.get(bill_id).file_identifier

    def get_positions(self, bill_id: BillId) -> List[Position]:
        return self._bill_store.get(bill_id).positions

    def add_position(self, bill_id: BillId, position: Position, index: int | None = None) -> None:
        """Add a position to the bill and optionally specify the index in the list of positions."""
        bill = self._bill_store.get(bill_id)
        if index is None:
            index = len(bill.positions)
        bill.add_position(position, index)

    def delete_position(self, bill_id: BillId, index: int) -> None:
        """Delete position at given index."""
        self._bill_store.get(bill_id).delete_position(index)
