from pathlib import Path

from co2data.bills.bill_data_provider import BillDataProvider
from co2data.bills.persistent_bill_data_provider import PersistentBillDataProvider
from co2data.bills.persistent_bill_store import PersistentBillStore
from co2data.pdf.directory_importer import import_bills_in_directory
from co2data.pdf.pdf_store import PdfStore


def create_bill_data_provider(pdf_store: PdfStore,
                              bills_directory: Path = Path("../dav_bills/"),
                              state_file: Path = Path("../data/saved_bill_data.json")) -> BillDataProvider:
    if state_file.exists():
        bill_store = PersistentBillStore.load(state_file)
    else:
        bill_store = PersistentBillStore(state_file)
    import_bills_in_directory(pdf_store, bill_store, bills_directory)
    return PersistentBillDataProvider(bill_store)
