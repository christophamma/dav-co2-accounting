from pathlib import Path
from typing import List

from co2data.bills.bill import Bill
from co2data.bills.concrete_bill_store import ConcreteBillStore


class PersistentBillStore(ConcreteBillStore):
    def __init__(self, filepath: Path, list_of_bills: List[Bill] = ()):
        super().__init__(list_of_bills)
        self._file_path = filepath

    def save(self):
        json = Bill.list_to_json(list(self.bills.values()))
        with open(self._file_path, "w", encoding="utf-8") as file_pointer:
            file_pointer.write(json)

    @classmethod
    def load(cls, file_path: Path):
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as file_pointer:
                raw_json = file_pointer.read()
            list_of_bills = Bill.from_json(raw_json)
            return cls(file_path, list_of_bills)

