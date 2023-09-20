from dataclasses import dataclass
from typing import Optional


@dataclass
class Category:
    area: str
    name: str
    example: str
    unit: str
    description: Optional[str] = None
