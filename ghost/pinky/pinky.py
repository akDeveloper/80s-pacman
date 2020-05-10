from ghost.ghost import Ghost
from ghost.pinky.pinky_animator import PinkyAnimator
from ghost.behaviour.chase.chase_ambush import ChaseAmbush
from ghost.behaviour.scatter.scatter import Scatter
from pygame import Rect


class Pinky(Ghost):
    COLOR = (255, 192, 203)
    SCATTER_CORNER = Rect(16, 0, 8, 8)

    def __init__(self, pacman, platforms, *groups):
        x = 100
        y = 116
        self.speed = 2
        super().__init__(x,  y, self.COLOR, pacman, platforms, *groups)
        self.chase = ChaseAmbush(self)
        self.scatter = Scatter(self, self.SCATTER_CORNER)
        self.motion.set_direction(-1)

    def get_speed(self):
        return self.speed

    def get_animator(self):
        return PinkyAnimator(self.factory)


