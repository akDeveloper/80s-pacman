from ghost.ghost import Ghost
from ghost.behaviour.chase.chase_aggresive import ChaseAggresive


class Blinky(Ghost):
    def __init__(self, pacman, platforms, *groups):
        x = 108
        y = 112
        self.speed = 2
        super().__init__(x,  y, 8, 8, (255, 0, 0), platforms, *groups)
        self.chase = ChaseAggresive(self, pacman)
        self.motion.set_direction(-1)

    def get_name(self):
        return "Blinky"

    def get_speed(self):
        return self.speed
