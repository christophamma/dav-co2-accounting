from pathlib import Path
from typing import Dict, List

from co2data.bills.bill import Bill
from co2data.bills.bill_id import BillId
from co2data.bills.bill_store import BillStore
from co2data.pdf.pdf_store import PdfStore


class ConcreteBillStore(BillStore):

    def __init__(self, pdf_store: PdfStore):
        self.first_id = 1000
        self.pdf_store = pdf_store
        self.bills: Dict[BillId, Bill] = {}

    def get(self, bill_id: BillId) -> Bill:
        return self.bills[bill_id]
    def all(self) -> List[BillId]:
        return list(self.bills.keys())

    def add_pdf(self, pdf_path: Path) -> BillId:
        file_identifier = pdf_path.name
        self.pdf_store.add_file(file_identifier, pdf_path)
        bill_id = max(self.bills.keys()) + 1 if len(self.bills.keys()) > 0 else self.first_id
        bill = Bill(bill_id, file_identifier, [])
        self.bills[bill_id] = bill
        return bill_id

