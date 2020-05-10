from ghost.ghost import Ghost
from ghost.pinky.pinky_animator import PinkyAnimator
from ghost.behaviour.chase.chase_ambush import ChaseAmbush
from ghost.behaviour.scatter.scatter import Scatter
from pygame import Rect


class Pinky(Ghost):
    COLOR = (255, 0, 0)
    SCATTER_CORNER = Rect(16, 0, 8, 8)

    def __init__(self, pacman, platforms, *groups):
        x = 100
        y = 116
        self.speed = 2
        super().__init__(x,  y, self.COLOR, platforms, *groups)
        self.chase = ChaseAmbush(self, self.calculate_pacman_rect(pacman))
        self.scatter = Scatter(self, self.SCATTER_CORNER)

        self.motion.set_direction(-1)

    def get_speed(self):
        return self.speed

    def get_animator(self):
        return PinkyAnimator(self.factory)

    def calculate_pacman_rect(self, pacman):
        facing = pacman.motion.current_dir
        rect = pacman.motion.rect
        delta = 32  # 4 tiles away from the direction of pacman
        if abs(facing) > 1:
            facing = facing / 2
            return rect.move(0, facing * delta)
        return rect.move(facing * delta, 0)
