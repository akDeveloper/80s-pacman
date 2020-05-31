from enum import Enum


class State(Enum):
    CHASE = 1
    SCATTER = 2
    FRIGHTENED = 3
    IN_HOUSE = 4
    LEAVING_HOUSE = 5
