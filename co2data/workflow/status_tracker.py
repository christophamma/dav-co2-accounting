from __future__ import annotations

import json
from enum import Enum
from pathlib import Path
from typing import List, Dict

import jsonpickle

from co2data.bills.bill import Bill
from co2data.bills.bill_id import BillId
from co2data.bills.bill_store import BillStore

class Status(Enum):
    TO_DO = 1
    IN_PROGRESS = 2
    DONE = 3

class StatusTracker:
    """
    Tracks the current workflow status of bills.
    """
    def __init__(self,
                 bill_status: Dict[BillId, Status]) -> None:
        self.bill_status = bill_status

    def get_by_status(self, status: Status) -> List[BillId]:
        """
        Get the list of all Bill Ids with the given status.
        :param status: status to filter for
        :return: List of Bill Ids
        """
        return [bill_id for bill_id in self.bill_status.keys() if self.bill_status[bill_id] == status]

    def set_status(self, bill_id: BillId, status: Status) -> None:
        """
        Set the status of a bill.
        :param bill_id: Bill id to set status for
        :param status: new status
        """
        self.bill_status[bill_id] = status

    

    @classmethod
    def load(cls, file_path: Path) -> StatusTracker:
        with open(file_path, "r", encoding="utf-8") as filehandle:
            bill_status = json.load(filehandle)
        return StatusTracker(bill_status)

