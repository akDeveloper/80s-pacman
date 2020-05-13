from ghost.ghost import Ghost
from ghost.inky.inky_animator import InkyAnimator
from ghost.behaviour.chase.chase_bashful import ChaseBashful
from ghost.behaviour.scatter.scatter import Scatter
from pygame import Rect


class Inky(Ghost):
    COLOR = (0, 100, 100)
    SCATTER_CORNER = Rect(208, 264, 8, 8)

    def __init__(self, pacman, blinky, platforms, *groups):
        x = 100
        y = 116
        self.speed = 2
        super().__init__(x,  y, self.COLOR, pacman, platforms, *groups)
        self.chase = ChaseBashful(self)
        self.blinky = blinky
        self.scatter = Scatter(self, self.SCATTER_CORNER)
        self.motion.set_direction(-1)

    def get_speed(self):
        return self.speed

    def get_animator(self):
        return InkyAnimator(self.factory)
