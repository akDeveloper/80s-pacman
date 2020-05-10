from ghost.behaviour.target_locator import TargetLocator
from ghost.behaviour.chase.chase_behaviour import ChaseBehaviour


class ChaseAmbush(ChaseBehaviour):

    def __init__(self, ghost, target):
        self.ghost = ghost
        self.target = target
        self.locator = TargetLocator(ghost, target)

    def chase(self):
        dir = self.locator.get_direction()
        self.ghost.motion.set_direction(dir)