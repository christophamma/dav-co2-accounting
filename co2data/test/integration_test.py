import os
from pathlib import Path

from co2data.bills.bill import Position
from co2data.bills.bill_data_provider_factory import create_bill_data_provider
from co2data.bills.bill_status import BillStatus
from co2data.categories.importer import create_category_provider_from_directory
from co2data.departments.department_provider import DepartmentProvider
from co2data.pdf.file_system_pdf_store import FileSystemPdfStore

if __name__ == "__main__":
    category_provider = create_category_provider_from_directory(Path("../../data/categories"))
    department_provider = DepartmentProvider.create_from_text_file(Path("../../data/departments.txt"))
    pdf_store = FileSystemPdfStore()
    bill_data_provider = create_bill_data_provider(pdf_store, bills_dir=Path("../../dav_bills/"))
    test_bill_id = bill_data_provider.bill_ids[1]
    print(test_bill_id)
    category = category_provider.get_all()[0]
    print(category)
    position = Position(category, department_provider.departments[0], 11, 1, 0, 0)
    bill_data_provider.add_position(test_bill_id, position)
    bill_data_provider.add_comment(test_bill_id, "test comment")
    bill_data_provider.set_status(test_bill_id, BillStatus.IN_PROGRESS)
    print(bill_data_provider.get_positions(test_bill_id))
    print(bill_data_provider.get_by_status(BillStatus.IN_PROGRESS))
    print(bill_data_provider.get_comment(test_bill_id))

    ## load the saved data again
    bill_data_provider_reload = create_bill_data_provider(pdf_store, bills_dir=Path("../../dav_bills/"))
    print(bill_data_provider_reload.bill_ids)
    print(bill_data_provider.get_positions(test_bill_id))
    print(bill_data_provider.get_by_status(BillStatus.IN_PROGRESS))
    print(bill_data_provider.get_comment(test_bill_id))
