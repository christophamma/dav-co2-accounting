from pathlib import Path
from typing import Dict

import jsonpickle

from co2data.bills.bill_id import BillId
from co2data.workflow.status_tracker import StatusTracker, Status


class PersistentStatusTracker(StatusTracker):
    """StatusTracker that writes status to file for each state change"""

    def __init__(self, bill_status: Dict[BillId, Status], status_file: Path) -> None:
        super().__init__(bill_status)
        self._status_file = status_file
        if status_file.exists():
            self.load(status_file)
            print(f"loaded bill status from file {status_file}: {bill_status}")
        

    def set_status(self, bill_id: BillId, status: Status) -> None:
        super().set_status(bill_id, status)
        self.save(self._status_file)

    def save(self, file_path: Path) -> None:
        """
        Save the status of all Bills to a file
        :param file_path: path to output file
        """
        with open(file_path, "w", encoding="utf-8") as filehandle:
            filehandle.write(jsonpickle.encode(self.bill_status))

    def load(self, file_path: Path) -> None:
        with open(file_path, "r", encoding="utf-8") as filehandle:
            loaded_status = jsonpickle.decode(filehandle.read())
        for bill_id in loaded_status:
            self.bill_status[int(bill_id)] = loaded_status[bill_id]
