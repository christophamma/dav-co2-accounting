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
        """Return Category by name"""
