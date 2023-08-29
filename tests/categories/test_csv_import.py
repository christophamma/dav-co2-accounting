from co2data.categories.category import Category
from co2data.categories.importer import import_csv


class TestCategoryImport:
    data = ['DATENPUNKT;BESCHREIBUNG;BEISPIEL;EINHEIT',
            ';;;',
            'Papier - Frischfaser;Kauf von Frischfaser-Papier für z. B. Drucker;5;kg',
            'Papier - Recycling;Kauf von Recycling-Papier für z. B. Drucker;5;kg',
            'Drucksachen - Frischfaser;Kauf von bedruckten Frischfaser-Papier Produkten (Drucksachen durch Druckereien);5;kg',
            'Drucksachen - Kunststoff;Kauf von bedruckten Kunststoff Produkten;5;kg',
            'Drucksachen - Textil;Kauf von bedruckten Textilien Produkten;5;kg',
            'Büromaterial (kg);Sonstige Ausgaben zum Bürobedarf und Batterien (z.B. kleinere Produkte, wie Scheren, Locher, Hefter oder Spitzer und Toner genauso wie Ordner, Mappen für die Ablage und Versandmaterial. Auch Schreibartikel wie Stifte und Schreibunterlagen zählen dazu.);10;kg',
            'Büromöbel (kg);Ausgaben für Büromöbel z.B. Schreibtisch, Schreibtischstuhl;20;kg']


    def test_create_category_provider_from_csv(self):
        expected = [Category('Papier - Frischfaser', 'kg', 'Kauf von Frischfaser-Papier für z. B. Drucker'),
                    Category('Papier - Recycling', 'kg', 'Kauf von Recycling-Papier für z. B. Drucker'),
                    Category('Drucksachen - Frischfaser', 'kg', 'Kauf von bedruckten Frischfaser-Papier Produkten (Drucksachen durch Druckereien)'),
                    Category('Drucksachen - Kunststoff', 'kg', 'Kauf von bedruckten Kunststoff Produkten'),
                    Category('Drucksachen - Textil', 'kg', 'Kauf von bedruckten Textilien Produkten'),
                    Category('Büromaterial (kg)', 'kg', 'Sonstige Ausgaben zum Bürobedarf und Batterien (z.B. kleinere Produkte, wie Scheren, Locher, Hefter oder Spitzer und Toner genauso wie Ordner, Mappen für die Ablage und Versandmaterial. Auch Schreibartikel wie Stifte und Schreibunterlagen zählen dazu.)'),
                    Category('Büromöbel (kg)', 'kg', 'Ausgaben für Büromöbel z.B. Schreibtisch, Schreibtischstuhl')]
        imported = import_csv(self.data)
        assert imported == expected