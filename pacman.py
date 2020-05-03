from pygame.sprite import Sprite
from entity import Entity
from motion import Motion
from factory.pacman_image_factory import PacmanImageFactory


class Pacman(Sprite):
    def __init__(self, pos, platforms, *groups):
        super().__init__(*groups)
        self.__draw_sprite()
        self.rect = self.image.get_rect(center=pos)
        self.col = Entity(self.rect.x+2, self.rect.y+2, 8, 8, (255, 0, 0))
        self.speed = 2
        self.motion = Motion(self.col, self.speed, platforms)
        self.motion.move_left()

    def update(self):
        self.motion.update()
        self.rect.center = self.col.rect.center

    def move_left(self):
        self.motion.set_direction(-1)

    def move_right(self):
        self.motion.set_direction(1)

    def move_up(self):
        self.motion.set_direction(-2)

    def move_down(self):
        self.motion.set_direction(2)

    def reset_x(self):
        self.motion.reset_x()

    def reset_y(self):
        self.motion.reset_y()

    def __draw_sprite(self):
        f = PacmanImageFactory()
        f.create()
        self.image = f.get_image(0)
