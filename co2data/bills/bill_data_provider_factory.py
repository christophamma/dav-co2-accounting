from pathlib import Path

from co2data.bills.bill_data_provider import BillDataProvider
from co2data.bills.concrete_bill_store import ConcreteBillStore
from co2data.bills.persistent_bill_data_provider import PersistentBillDataProvider
from co2data.bills.persistent_bill_store import PersistentBillStore
from co2data.pdf.directory_importer import import_bills_in_directory
from co2data.pdf.pdf_store import PdfStore


def create_bill_data_provider(pdf_store: PdfStore, bills_directory: Path = Path("../dav_bills/")) -> BillDataProvider:
    bill_store = PersistentBillStore(Path("../data/saved_bill_data.json"))
    import_bills_in_directory(pdf_store, bill_store, bills_directory)
    return PersistentBillDataProvider(bill_store)
