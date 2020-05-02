from pygame.sprite import Sprite
from pygame import Surface
from pygame import SRCALPHA
from pygame import gfxdraw
from entity import Entity
from motion import Motion


class Pacman(Sprite):
    def __init__(self, pos, platforms, *groups):
        super().__init__(*groups)
        self.__draw_sprite()
        self.rect = self.image.get_rect(center=pos)
        self.col = Entity(self.rect.x+2, self.rect.y+2, 8, 8, (255, 0, 0))
        self.speed = 2
        self.motion = Motion(self.col, self.speed, platforms)

    def update(self):
        self.motion.update()
        self.rect.center = self.col.rect.center

    def move_left(self):
        self.motion.move_left()

    def move_right(self):
        self.motion.move_right()

    def move_up(self):
        self.motion.move_up()

    def move_down(self):
        self.motion.move_down()

    def reset_x(self):
        self.motion.reset_x()

    def reset_y(self):
        self.motion.reset_y()

    def __draw_sprite(self):
        yellow = (255, 255, 0)
        self.image = Surface((13, 13), SRCALPHA)
        gfxdraw.aacircle(self.image, 6, 6, 5, yellow)
        gfxdraw.filled_circle(self.image, 6, 6, 5, yellow)
