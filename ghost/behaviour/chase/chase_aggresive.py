from ghost.behaviour.target_locator import TargetLocator
from ghost.behaviour.behaviour import Behaviour
from pygame import Rect


class ChaseAggresive(Behaviour):

    def __init__(self, ghost, pacman):
        self.ghost = ghost
        self.locator = TargetLocator(ghost)
        self.target = None
        self.pacman = pacman

    def execute(self, time: int):
        self.locator.set_reverse(self.ghost.state_changed)
        self.target = self.pacman.col.rect
        dir = self.locator.get_direction(self.target)
        self.ghost.motion.set_direction(dir)

    def get_target(self) -> Rect:
        return self.target
