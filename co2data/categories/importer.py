import csv
from typing import TextIO, List

from co2data.categories.category import Category


def import_csv(csv_file: TextIO) -> List[Category]:
    """Create a CategoryProvider instance initialized with all categories given in csv file"""
    csv_name = 'DATENPUNKT'
    csv_description = 'BESCHREIBUNG'
    csv_example = 'BEISPIEL'
    csv_unit = 'EINHEIT'
    category_reader = csv.DictReader(csv_file, delimiter=';')
    categories = []
    for row in category_reader:
        if row[csv_name] != '':
            categories.append(Category(row[csv_name], row[csv_unit], row[csv_description]))
    return categories
