from entity import Entity
from ghost.method_not_implemented import MethodNotImplemented
from ghost.state import State


class Ghost(Entity):
    def __init__(self, x, y, w, h, color, *groups):
        super().__init__(x, y, w, h, color, *groups)
        self.state = State.CHASE
        self.chase = None
        self.scatter = None
        self.frightened = None

    def get_name(self):
        raise MethodNotImplemented("Implement `get_name` method")

    def update(self):
        pass

    def move_to(self, tile):
        pass
