from ghost.behaviour.target_locator import TargetLocator
from ghost.behaviour.scatter.scatter_behaviour import ScatterBehaviour


class ScatterTopright(ScatterBehaviour):
    def __init__(self, ghost, target):
        self.ghost = ghost
        self.target = target
        self.locator = TargetLocator(ghost, target)

    def scatter(self):
        dir = self.locator.get_direction()
        self.ghost.motion.set_direction(dir)
