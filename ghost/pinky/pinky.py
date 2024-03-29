from ghost.ghost import Ghost
from ghost.pinky.pinky_animator import PinkyAnimator
from ghost.behaviour.chase.chase_ambush import ChaseAmbush
from ghost.behaviour.scatter.scatter import Scatter
from pygame import Rect
from ghost.state import State
from pacman import Pacman
from pygame.sprite import Group
from ghost.behaviour.in_house import InHouse


class Pinky(Ghost):
    COLOR = (255, 192, 203)
    SCATTER_CORNER = Rect(16, 0, 8, 8)

    def __init__(self, pacman: Pacman, platforms: Group, *groups):
        x = 114
        y = 142
        self.speed = 2
        super().__init__(x,  y, self.COLOR, pacman, platforms, *groups)
        self.chase = ChaseAmbush(self, pacman)
        self.scatter = Scatter(self, self.SCATTER_CORNER)
        self.in_house = InHouse(self)
        self.motion.set_direction(-1)
        self.state = self.in_house
        self.state_name = State.IN_HOUSE

    def get_speed(self) -> int:
        return self.speed

    def get_animator(self) -> PinkyAnimator:
        return PinkyAnimator(self.factory)
