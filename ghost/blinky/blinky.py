from ghost.ghost import Ghost
from ghost.blinky.blinky_animator import BlinkyAnimator
from ghost.behaviour.chase.chase_aggresive import ChaseAggresive


class Blinky(Ghost):
    COLOR = (255, 0, 0)

    def __init__(self, pacman, platforms, *groups):
        x = 108
        y = 112
        self.speed = 2
        super().__init__(x,  y, self.COLOR, platforms, *groups)
        self.chase = ChaseAggresive(self, pacman.col.rect)
        self.motion.set_direction(-1)

    def get_speed(self):
        return self.speed

    def get_animator(self):
        return BlinkyAnimator(self.factory)
