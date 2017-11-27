from enum import Enum, unique


@unique
class Timestamp(Enum):
    QUARTERS = 1
    HOURS = 2
    DAYS = 3
