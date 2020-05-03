from entity import Entity
from ghost.method_not_implemented import MethodNotImplemented
from ghost.state import State
from motion import Motion
from pygame.time import Clock


class Ghost(Entity):
    def __init__(self, x, y, w, h, color, platforms, *groups):
        super().__init__(x, y, w, h, color, *groups)
        self.state = State.CHASE
        self.chase = None
        self.scatter = None
        self.frightened = None
        self.motion = Motion(self, self.get_speed(), platforms)
        self.clock = Clock()

    def get_name(self):
        raise MethodNotImplemented("Implement `get_name` method")

    def get_speed(self):
        raise MethodNotImplemented("Implement `get_speed` method")

    def update(self, time):
        self.chase.chase()
        self.motion.update()
