from pathlib import Path

from co2data.bills.bill_store import BillStore
from co2data.pdf.pdf_store import PdfStore


def import_bills_in_directory(pdf_store: PdfStore, bill_store: BillStore, directory: Path) -> None:
    """
    Add all bills in directory to the BillStore.
    :param bill_store:
    :param directory:
    :return:
    """
    for pdf_file in directory.glob("*.pdf"):
        file_identifier = pdf_file.name
        if pdf_store.has(file_identifier):
            print(f"skip {pdf_file}, already present in store.")
        else:
            pdf_store.add_file(file_identifier, pdf_file)
        bill_store.add(file_identifier)
        #print(f"adding {pdf_file} with id {bill_id}")