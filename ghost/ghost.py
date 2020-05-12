from entity import Entity
from motion import Motion
from ghost.state import State
from pygame.sprite import Sprite
from factory.ghost_image_factory import GhostImageFactory
from ghost.method_not_implemented import MethodNotImplemented


class Ghost(Sprite):
    WIDTH = 14
    HEIGHT = 14

    def __init__(self, x, y, color, pacman, platforms, *groups):
        super().__init__(*groups)
        self.state = State.SCATTER
        self.chase = None
        self.scatter = None
        self.frightened = None
        self.pacman = pacman
        self.factory = GhostImageFactory()
        self.factory.create()
        self.animator = self.get_animator()
        self.image = self.animator.next(0)
        self.rect = self.image.get_rect(center=(x, y))
        self.col = Entity(self.rect.x+3, self.rect.y+3, 8, 8, color, groups[2])
        self.loc = Entity(self.rect.x+3, self.rect.y+3, 8, 8, color, groups[2])
        self.motion = Motion(self.col, self.get_speed(), platforms)

    def kill(self):
        self.col.kill()
        self.loc.kill()
        super().kill()

    def get_speed(self):
        raise MethodNotImplemented("Implement `get_speed` method")

    def get_animator(self):
        raise MethodNotImplemented("Implement `get_factory` method")

    def update(self, time):
        if self.pacman.alive is False:
            return

        if self.state == State.CHASE:
            self.chase.chase(self.pacman)
            self.loc.rect = self.chase.target
        elif self.state == State.SCATTER:
            self.scatter.scatter()
            self.loc.rect = self.scatter.target

        if self.motion.should_move_to_x():
            self.motion.reset_y()
        elif self.motion.should_move_to_y():
            self.motion.reset_x()
        self.motion.update()
        self.rect.center = self.col.rect.center
        self.motion.check_current_direction()
        self.image = self.animator.next(self.motion.current_dir)
