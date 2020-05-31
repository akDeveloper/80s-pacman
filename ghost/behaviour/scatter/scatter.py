from ghost.behaviour.target_locator import TargetLocator
from ghost.behaviour.behaviour import Behaviour
from pygame import Rect
from ghost.ghost import Ghost


class Scatter(Behaviour):
    SPEED = 2

    def __init__(self, ghost: Ghost, target: Rect):
        self.ghost = ghost
        self.target = target
        self.locator = TargetLocator(ghost)

    def execute(self, time: int):
        self.ghost.motion.speed = self.SPEED
        dir = self.locator.get_direction(self.target)
        self.ghost.motion.set_direction(dir)

    def get_target(self) -> Rect:
        return self.target
