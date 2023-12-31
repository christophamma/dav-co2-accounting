from typing import List

from co2data.bills.bill import Position
from co2data.bills.bill_id import BillId
from co2data.bills.bill_status import BillStatus
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

    def move_position_up(self, bill_id: BillId, index: int) -> None:
        """Move position at given index up towards start of list by one."""
        bill = self._bill_store.get(bill_id)
        if index > 0:
            new_index = index - 1
            bill.positions.insert(new_index, bill.positions.pop(index))

    def move_position_down(self, bill_id: BillId, index: int) -> None:
        """Move position at given index down towards end of list by one."""
        bill = self._bill_store.get(bill_id)
        if index <= len(bill.positions) - 2:
            new_index = index + 1
            bill.positions.insert(new_index, bill.positions.pop(index))

    def get_by_status(self, status: BillStatus) -> List[BillId]:
        """
        Get the list of all Bill Ids with the given status.
        :param status: status to filter for
        :return: List of Bill Ids
        """
        return [bill_id for bill_id in self.bill_ids if self._bill_store.get(bill_id).status == status]

    def set_status(self, bill_id: BillId, status: BillStatus) -> None:
        """
        Set the status of a bill.
        :param bill_id: Bill id to set status for
        :param status: new status
        """
        self._bill_store.get(bill_id).status = status

    def get_status(self, bill_id: BillId) -> BillStatus:
        """
        Return the bill status.
        :param bill_id: Bill id to get status for
        """
        return self._bill_store.get(bill_id).status

    def add_comment(self, bill_id: BillId, comment: str) -> None:
        """
        Add a comment to the bill, existing comment will be overwritten.

        :param bill_id: bill id to add comment to.
        :param comment: comment to add
        """
        self._bill_store.get(bill_id).comment = comment

    def get_comment(self, bill_id: BillId) -> str:
        """
        Retrieve comment for the given bill id.

        :param bill_id: bill id
        """
        return self._bill_store.get(bill_id).comment
