from ghost.behaviour.target_locator import TargetLocator
from ghost.behaviour.behaviour import Behaviour
from pygame import Rect


class ChaseAmbush(Behaviour):

    def __init__(self, ghost, pacman):
        self.ghost = ghost
        self.locator = TargetLocator(ghost)
        self.target = None
        self.pacman = pacman

    def execute(self, time: int):
        ''' Return void '''
        self.target = self.calculate_target_rect()
        dir = self.locator.get_direction(self.target)
        self.ghost.motion.set_direction(dir)

    def get_target(self) -> Rect:
        return self.target

    def calculate_target_rect(self):
        ''' Return Rect '''
        if self.pacman.motion.current_dir != 0:
            facing = self.pacman.motion.current_dir
        else:
            facing = self.pacman.motion.dir
        rect = self.pacman.motion.rect
        delta = 32  # 4 tiles away from the direction of pacman
        if abs(facing) > 1:
            facing = facing / 2
            return rect.move(0, facing * delta)
        return rect.move(facing * delta, 0)
