import json
from pathlib import Path

import jsonpickle

from co2data.bills.bill import Position
from co2data.bills.bill_data_provider import BillDataProvider
from co2data.bills.bill_id import BillId
from co2data.bills.bill_status import BillStatus
from co2data.bills.bill_store import BillStore
from co2data.bills.persistent_bill_store import PersistentBillStore


class PersistentBillDataProvider(BillDataProvider):
    """Bill data provider, that writes every state change to a file."""

    def __init__(self, bill_store: PersistentBillStore) -> None:
        super().__init__(bill_store)

    def add_position(self, bill_id: BillId, position: Position, index: int | None = None) -> None:
        super().add_position(bill_id, position, index)
        self._bill_store.save()

    def delete_position(self, bill_id: BillId, index: int) -> None:
        super().delete_position(bill_id, index)
        self._bill_store.save()

    def set_status(self, bill_id: BillId, status: BillStatus) -> None:
        super().set_status(bill_id, status)
        self._bill_store.save()

    
 
