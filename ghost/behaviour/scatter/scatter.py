from ghost.behaviour.target_locator import TargetLocator
from ghost.behaviour.scatter.scatter_behaviour import ScatterBehaviour


class Scatter(ScatterBehaviour):
    def __init__(self, ghost, target):
        '''
        ghost -- Ghost
        target -- Rect
        '''
        self.ghost = ghost
        self.target = target
        self.locator = TargetLocator(ghost)

    def scatter(self):
        dir = self.locator.get_direction(self.target)
        self.ghost.motion.set_direction(dir)
