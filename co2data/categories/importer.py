import csv
from pathlib import Path
from typing import TextIO, List

from co2data.categories.category import Category
from co2data.categories.category_provider import CategoryProvider
from co2data.categories.concrete_category_provider import ConcreteCategoryProvider


def create_category_provider_from_directory(directory: Path) -> CategoryProvider:
    categories = []
    for csv_file in directory.glob("*.csv"):
        with open(csv_file, "r", encoding="utf-8") as filehandle:
            categories.extend(import_csv(filehandle, csv_file.stem))
    return ConcreteCategoryProvider(categories)


def import_csv(csv_file: TextIO, area: str) -> List[Category]:
    """
    Read a list of categories from a csv file.

    The csv file is expected to have the column headers 'Datenpunkt', 'Beschreibung', 'Beispiel' and 'Einheit' in the
    first row.
    The delimiter must be a semicolon.

    :param csv_file: TextIO object to read data from
    :param area: Name of the category area for this file
    """
    csv_name = 'Datenpunkt'
    csv_description = 'Beschreibung'
    csv_example = 'Beispiel'
    csv_unit = 'Einheit'
    category_reader = csv.DictReader(csv_file, delimiter=';')
    categories = []
    for row in category_reader:
        if row[csv_name] != '':
            categories.append(Category(area, row[csv_name], row[csv_example], row[csv_unit], row[csv_description]))
    return categories
