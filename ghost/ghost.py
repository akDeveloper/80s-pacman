from entity import Entity
from motion import Motion
from pygame.sprite import Sprite
from factory.ghost_image_factory import GhostImageFactory
from ghost.method_not_implemented import MethodNotImplemented
from ghost.state import State


class Ghost(Sprite):
    WIDTH = 14
    HEIGHT = 14

    def __init__(self, x, y, color, pacman, platforms, *groups):
        super().__init__(*groups)
        self.chase = None
        self.scatter = None
        self.frightened = None
        self.pacman = pacman
        self.factory = GhostImageFactory()
        self.factory.create()
        self.animator = self.get_animator()
        self.image = self.animator.next(0)
        self.rect = self.image.get_rect(center=(x, y))
        ''' The collision detection sprite '''
        self.col = Entity(self.rect.x+3, self.rect.y+3, 8, 8, color, groups[2])
        ''' The location detection sprite '''
        self.loc = Entity(self.rect.x+3, self.rect.y+3, 8, 8, color, groups[2])
        self.doors = groups[3]
        self.motion = Motion(self.col, self.get_speed(), platforms)
        self.state_changed = False

    def kill(self):
        self.col.kill()
        self.loc.kill()
        super().kill()

    def set_state(self, state: int):
        raise MethodNotImplemented("Implement `set_state` method")

    def get_state():
        raise MethodNotImplemented("Implement `get_state` method")

    def get_speed(self):
        raise MethodNotImplemented("Implement `get_speed` method")

    def get_animator(self):
        raise MethodNotImplemented("Implement `get_factory` method")

    def get_state_name(self) -> str:
        raise MethodNotImplemented("Implement `get_state_name` method")

    def update(self, time):
        if self.pacman.alive is False:
            self.image = self.animator.next(self.motion.current_dir)
            return

        self.get_state().execute(time)
        self.loc.rect = self.get_state().get_target()
        if self.motion.should_move_to_x():
            self.motion.reset_y()
        elif self.motion.should_move_to_y():
            self.motion.reset_x()
        self.motion.update(self.get_state_name() == State.IN_HOUSE)
        self.rect.center = self.col.rect.center
        self.motion.check_current_direction()
        self.image = self.animator.next(self.motion.current_dir)

    def is_in_house(self) -> bool:
        return self.get_state_name() == State.IN_HOUSE \
            and self.col.rect.bottom > 120
