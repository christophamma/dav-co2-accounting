from pathlib import Path

from co2data.pdf.ConcretePageProvider import ConcretePageProvider
from co2data.pdf.file_system_pdf_store import FileSystemPdfStore


def main():
    pdf_path = Path("../../dav_bills")
    pdf_store = FileSystemPdfStore()
    for pdf_file in pdf_path.glob("*.pdf"):
        file_identifier = pdf_file.name
        if pdf_store.has(file_identifier):
            pass
        else:
            pdf_store.add_file(file_identifier, pdf_file)
    print(pdf_store.files)
    page_provider = ConcretePageProvider(pdf_store)
    file_identifier = list(pdf_store.files.keys())[0]
    nr_pages = page_provider.get_nr_of_pages(file_identifier)
    print(f"{file_identifier} has {nr_pages} pages")
    page_1 = page_provider.get_page(file_identifier, 0)
    page_2 = page_provider.get_page(file_identifier, 1)
    page_1.save(filename=f"{file_identifier}.page1.jpg")
    page_2.save(filename=f"{file_identifier}.page2.jpg")



if __name__ == "__main__":
    main()
