from ghost.behaviour.target_locator import TargetLocator
from ghost.behaviour.chase.chase_behaviour import ChaseBehaviour


class ChaseAmbush(ChaseBehaviour):

    def __init__(self, ghost):
        self.ghost = ghost
        self.locator = TargetLocator(ghost)
        self.target = None

    def chase(self, pacman):
        self.target = self.calculate_target_rect(pacman)
        dir = self.locator.get_direction(self.target)
        self.ghost.motion.set_direction(dir)

    def calculate_target_rect(self, pacman):
        if pacman.motion.current_dir != 0:
            facing = pacman.motion.current_dir
        else:
            facing = pacman.motion.dir
        rect = pacman.motion.rect
        delta = 32  # 4 tiles away from the direction of pacman
        if abs(facing) > 1:
            facing = facing / 2
            return rect.move(0, facing * delta)
        return rect.move(facing * delta, 0)
