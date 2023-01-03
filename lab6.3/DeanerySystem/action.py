from enum import Enum


class Action(Enum):
    DAY_EARLIER = -1
    DAY_LATER = 1
    TIME_EARLIER = -2
    TIME_LATER = 2
