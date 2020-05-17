from ghost.ghost import Ghost
from ghost.pinky.pinky_animator import PinkyAnimator
from ghost.behaviour.chase.chase_ambush import ChaseAmbush
from ghost.behaviour.scatter.scatter import Scatter
from pygame import Rect
from ghost.state import State


class Pinky(Ghost):
    COLOR = (255, 192, 203)
    SCATTER_CORNER = Rect(16, 0, 8, 8)

    def __init__(self, pacman, platforms, *groups):
        x = 100
        y = 116
        self.speed = 2
        super().__init__(x,  y, self.COLOR, pacman, platforms, *groups)
        self.chase = ChaseAmbush(self, pacman)
        self.scatter = Scatter(self, self.SCATTER_CORNER)
        self.motion.set_direction(-1)
        self.__state = self.scatter

    def get_speed(self):
        return self.speed

    def get_animator(self):
        return PinkyAnimator(self.factory)

    def get_state(self):
        return self.__state

    def set_state(self, state: int):
        if state == State.SCATTER:
            self.__state = self.scatter
        elif state == State.CHASE:
            self.__state = self.chase
        self.state_changed = True
