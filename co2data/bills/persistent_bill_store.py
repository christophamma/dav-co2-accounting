from pathlib import Path
import jsonpickle
from co2data.bills.concrete_bill_store import ConcreteBillStore
from co2data.pdf.pdf_store import PdfStore


class PersistentBillStore(ConcreteBillStore):
    def __init__(self, filepath: Path):
        super().__init__()
        self._file_path = filepath
        self.load()

    def save(self):
        with open(self._file_path, "w", encoding="utf-8") as file_pointer:
            file_pointer.write(jsonpickle.encode(self.bills))

    def load(self):
        if self._file_path.exists():
            with open(self._file_path, "r", encoding="utf-8") as file_pointer:
                bills = jsonpickle.decode(file_pointer.read())
            bills_with_int_ids = {int(bill_id): bill for bill_id, bill in bills.items()}
            self.bills = bills_with_int_ids

