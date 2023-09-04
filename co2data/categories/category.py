from dataclasses import dataclass
from typing import Optional


@dataclass
class Category:
    name: str
    example: str
    unit: str
    description: Optional[str] = None
