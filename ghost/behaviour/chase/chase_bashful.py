from ghost.behaviour.target_locator import TargetLocator
from ghost.behaviour.behaviour import Behaviour
from pygame import Rect


class ChaseBashful(Behaviour):
    TILE_WIDTH = 8

    def __init__(self, ghost, pacman, blinky):
        self.ghost = ghost
        self.locator = TargetLocator(ghost)
        self.target = None
        self.pacman = pacman
        self.blinky = blinky

    def execute(self):
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
        '''
        2 tiles away from the direction of pacman
        '''
        delta = self.TILE_WIDTH * 2
        if abs(facing) > 1:
            facing = facing / 2
            pacman_rect = rect.move(0, facing * delta)
        else:
            pacman_rect = rect.move(facing * delta, 0)
        dX = pacman_rect.x - self.blinky.rect.x
        if dX < 0:
            dxMinus = True
        else:
            dxMinus = False
        dY = pacman_rect.y - self.blinky.rect.y
        if dY < 0:
            dyMinus = True
        else:
            dyMinus = False
        dxDouble = dX * 2
        if dxMinus:
            dxDouble = dxDouble * -1
        dyDouble = dY * 2
        if not dyMinus:
            dyDouble = dyDouble * -1
        return self.blinky.rect.move(dxDouble, dyDouble)
