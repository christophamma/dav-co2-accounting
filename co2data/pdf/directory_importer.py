from pathlib import Path

from co2data.bills.bill_store import BillStore


def import_bills_in_directory(bill_store: BillStore, directory: Path) -> None:
    """
    Add all bills in directory to the BillStore.
    :param bill_store:
    :param directory:
    :return:
    """
    for pdf_file in directory.glob("*.pdf"):
        bill_id = bill_store.add_pdf(pdf_file)
        #print(f"adding {pdf_file} with id {bill_id}")