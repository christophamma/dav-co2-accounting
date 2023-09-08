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
<<<<<<< Updated upstream
        bill_id = bill_store.add_pdf(pdf_file)
=======
        file_identifier = pdf_file.name
        if pdf_store.has(file_identifier):
            pass
        else:
            pdf_store.add_file(file_identifier, pdf_file)
        bill_store.add(file_identifier)
>>>>>>> Stashed changes
        #print(f"adding {pdf_file} with id {bill_id}")