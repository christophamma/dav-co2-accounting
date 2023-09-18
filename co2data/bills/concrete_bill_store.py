from typing import Dict, List
import logging

from co2data.bills.bill import Bill
from co2data.bills.bill_id import BillId
from co2data.bills.bill_status import BillStatus
from co2data.bills.bill_store import BillStore


class ConcreteBillStore(BillStore):

    def __init__(self, bills: List[Bill] = ()):
        self.first_id = 1000
        self.bills: Dict[BillId, Bill] = {bill.id: bill for bill in bills}

    def get(self, bill_id: BillId) -> Bill:
        return self.bills[bill_id]

    def all(self) -> List[BillId]:
        return list(self.bills.keys())

    def add(self, file_identifier: str):
        if file_identifier in [b.file_identifier for b in self.bills.values()]:
            logging.info(f"BillStore: file identifier {file_identifier} already present")
        else:
            bill_id = max(self.bills.keys()) + 1 if len(self.bills.keys()) > 0 else self.first_id
            bill = Bill(bill_id, file_identifier, [], BillStatus.TO_DO)
            self.bills[bill_id] = bill
