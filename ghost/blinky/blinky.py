from ghost.ghost import Ghost
from ghost.blinky.blinky_animator import BlinkyAnimator
from ghost.behaviour.chase.chase_aggresive import ChaseAggresive
from ghost.behaviour.scatter.scatter import Scatter
from pygame import Rect
from ghost.state import State
from pacman import Pacman
from pygame.sprite import Group


class Blinky(Ghost):
    COLOR = (255, 0, 0)
    SCATTER_CORNER = Rect(200, 0, 8, 8)

    def __init__(self, pacman: Pacman, platforms: Group, *groups):
        x = 112
        y = 116
        self.speed = 2
        super().__init__(x,  y, self.COLOR, pacman, platforms, *groups)
        self.chase = ChaseAggresive(self, pacman)
        self.scatter = Scatter(self, self.SCATTER_CORNER)
        self.motion.set_direction(-1)
        self.state = self.scatter
        self.state_name = State.SCATTER

    def get_speed(self) -> int:
        return self.speed

    def get_animator(self) -> BlinkyAnimator:
        return BlinkyAnimator(self.factory)
