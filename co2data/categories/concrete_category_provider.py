from typing import List

from co2data.categories.category import Category
from co2data.categories.category_provider import CategoryProvider


class ConcreteCategoryProvider(CategoryProvider):

    def get_by_name(self, name: str) -> Category:
        filtered = [category for category in self.categories if category.name == name]
        print(filtered)
        if len(filtered) == 1:
            return filtered[0]
        else:
            raise ValueError(f"{len(filtered)} categories found for name {name}")

    def __init__(self, categories: List[Category]):
        self.categories = categories

    def get_all(self) -> List[Category]:
        return self.categories

    def get_areas(self) -> List[str]:
        return list(sorted(set([category.area for category in self.categories])))

    def get_categories_for_area(self, area: str) -> List[Category]:
        return [category for category in self.categories if category.area == area]