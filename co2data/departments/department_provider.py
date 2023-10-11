from __future__ import annotations

from pathlib import Path
from typing import List


class DepartmentProvider:
    """Provide all available departments (Sektionsbereiche)."""

    def __init__(self, departments: List[str]) -> None:
        """
        Create instance.

        :param departments: list of departments.
        """
        self._departments = departments

    @property
    def departments(self) -> List[str]:
        """
        Return a list of all available departments
        """
        return self._departments

    @classmethod
    def create_from_text_file(cls, filepath: Path) -> DepartmentProvider:
        """
        Create instance from text file containing the departments given line by line.

        :param filepath: path to text file-
        """
        with filepath.open("r", encoding="utf-8") as filehandle:
            departments = [line.strip() for line in filehandle]
        return cls(departments)
