import logging
import os
import shutil
from datetime import datetime
from pathlib import Path

from co2data.bills.bill_data_provider import BillDataProvider
from co2data.bills.persistent_bill_data_provider import PersistentBillDataProvider
from co2data.bills.persistent_bill_store import PersistentBillStore
from co2data.pdf.directory_importer import import_bills_in_directory
from co2data.pdf.pdf_store import PdfStore

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)

def create_bill_data_provider(pdf_store: PdfStore,
                              bills_dir: Path = Path("../datadir/"),
                              state_file_name: Path = Path("saved_bill_data.json")) -> BillDataProvider:
    bills_directory = bills_dir.absolute()
    autosave_dir = bills_directory / ".autosave"
    state_file = autosave_dir / state_file_name
    logging.info(f"bills dir: {bills_directory} from ({bills_dir})")
    logging.info(f"autosave: {autosave_dir}")
    logging.info(f"state file: {state_file}")
    if state_file.exists():
        logging.info("statefile exists")
        now = datetime.now()
        backup_file = f"backup_bill_data_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}.json"
        shutil.copy(autosave_dir / state_file, autosave_dir / backup_file)
        bill_store = PersistentBillStore.load(autosave_dir / state_file)
    else:
        logging.info("statefile does not exist")
        if not autosave_dir.exists():
            os.makedirs(autosave_dir)
        bill_store = PersistentBillStore(autosave_dir / state_file)
    import_bills_in_directory(pdf_store, bill_store, bills_directory)
    return PersistentBillDataProvider(bill_store)
