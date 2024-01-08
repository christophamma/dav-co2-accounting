from dataclasses import dataclass
from typing import Optional


@dataclass
class Category:
    area: str
    name: str
    example: str
    unit: str
    description: Optional[str] = None
    emission_by_unit: Optional[float] = None
    emission_by_price: Optional[float] = None
