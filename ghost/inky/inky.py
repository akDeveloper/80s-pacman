from ghost.ghost import Ghost
from ghost.inky.inky_animator import InkyAnimator
from ghost.behaviour.chase.chase_bashful import ChaseBashful
from ghost.behaviour.scatter.scatter import Scatter
from pygame import Rect
from ghost.state import State
from pacman import Pacman
from pygame.sprite import Group
from ghost.blinky.blinky import Blinky
from ghost.behaviour.in_house import InHouse


class Inky(Ghost):
    COLOR = (0, 100, 100)
    SCATTER_CORNER = Rect(208, 264, 8, 8)

    def __init__(self,
                 pacman: Pacman,
                 blinky: Blinky,
                 platforms: Group,
                 *groups: tuple):
        x = 96
        y = 142
        self.speed = 2
        super().__init__(x,  y, self.COLOR, pacman, platforms, *groups)
        self.chase = ChaseBashful(self, pacman, blinky)
        self.scatter = Scatter(self, self.SCATTER_CORNER)
        self.in_house = InHouse(self)
        self.motion.set_direction(-2)
        self.state = self.in_house
        self.state_name = State.IN_HOUSE

    def get_speed(self) -> int:
        return self.speed

    def get_animator(self) -> InkyAnimator:
        return InkyAnimator(self.factory)
