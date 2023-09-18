from __future__ import annotations

from enum import Enum


class BillStatus(str, Enum):  # str makes it easily serializable with json
    TO_DO = "ToDo"
    IN_PROGRESS = "InProgress"
    DONE = "Done"
