from enum import Enum


class Currency(Enum):
    USD = f"{chr(36)}"
    RUR = f"{chr(8_381)}"


class Statuses(Enum):
    NEW = "blue"
    HANDLING = "yellow"
    HANDLED = "green"
    CANCELED = "red"
