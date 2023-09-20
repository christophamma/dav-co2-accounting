from abc import ABC, abstractmethod
from typing import List

from co2data.categories.category import Category


class CategoryProvider(ABC):
    """Provides the available categories to the system"""

    @abstractmethod
    def get_all(self) -> List[Category]:
        """Return a set of all available categories"""

    @abstractmethod
    def get_by_name(self, name: str) -> Category:
        """Return Category by name."""

    @abstractmethod
    def get_areas(self) -> List[str]:
        """Return all category areas."""

    @abstractmethod
    def get_categories_for_area(self, area: str) -> List[Category]:
        """Return all categories of a given area."""
