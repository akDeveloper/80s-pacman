from ghost.behaviour.target_locator import TargetLocator
from ghost.behaviour.chase.chase_behaviour import ChaseBehaviour


class ChaseAggresive(ChaseBehaviour):

    def __init__(self, ghost):
        self.ghost = ghost
        self.locator = TargetLocator(ghost)
        self.target = None

    def chase(self, pacman):
        self.locator.set_reverse(self.ghost.state_changed)
        self.target = pacman.col.rect
        dir = self.locator.get_direction(self.target)
        self.ghost.motion.set_direction(dir)
