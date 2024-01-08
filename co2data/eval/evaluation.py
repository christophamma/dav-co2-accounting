from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from co2data.bills.persistent_bill_store import PersistentBillStore


@dataclass
class DetailedPosition:
    bill_file: str
    category_name: str
    category_area: str
    category_unit: str
    department: str
    value: float
    amount: float
    price: float
    emission_by_unit: float
    emission_by_price: float
    bill_status: str


def load_data(datafile: Path) -> pd.DataFrame:
    bill_store = PersistentBillStore.load(datafile)
    bill_ids = bill_store.all()
    positions = []
    for bill_id in bill_ids:
        bill = bill_store.get(bill_id)
        for position in bill.positions:
            detailed_position = DetailedPosition(
                bill.file_identifier,
                position.category.name,
                position.category.area,
                position.category.unit,
                position.department,
                position.value,
                position.amount,
                position.price,
                position.category.emission_by_unit,
                position.category.emission_by_price,
                bill.status
            )
            positions.append(detailed_position)
    data_frame = pd.DataFrame(positions)
    return data_frame


def load_multiple_files(datafiles: list[Path]) -> pd.DataFrame:
    data_frames = [load_data(datafile) for datafile in datafiles]
    return pd.concat(data_frames, axis=0)

