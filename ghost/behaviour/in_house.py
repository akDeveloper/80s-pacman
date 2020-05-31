from ghost.behaviour.behaviour import Behaviour
from pygame import Rect
from ghost.ghost import Ghost
from itertools import cycle


class InHouse(Behaviour):
    SPEED = 1

    def __init__(self, ghost: Ghost):
        self.ghost = ghost
        self.dirs = cycle([-2, 2])

    def execute(self, time: int) -> None:
        self.ghost.motion.speed = self.SPEED
        if self.ghost.motion.current_dir == 0:
            dir = next(self.dirs)
            self.ghost.motion.set_direction(dir)

    def get_target(self) -> Rect:
        return Rect(92, 120, 8, 8)
