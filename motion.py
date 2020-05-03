from pygame.math import Vector2
from pygame.sprite import collide_rect


class Motion(object):
    def __init__(self, sprite, speed, platforms):
        self.speed = speed
        self.dir = 0
        self.prev_dir = 0
        self.vel = Vector2(0, 0)
        self.platforms = platforms
        self.rect = sprite.rect
        self.sprite = sprite
        self.collide_x = False
        self.collide_y = False
        self.current_dir = 0

    def update(self):
        self.check_x_axis_collide()
        self.check_y_axis_collide()
        self.check_teleporting()
        self.check_velocity()

    def check_x_axis_collide(self):
        self.rect.left += self.vel.x
        self.collide_x = False
        self.collide(self.vel.x, 0)

    def check_y_axis_collide(self):
        self.rect.top += self.vel.y
        self.collide_y = False
        self.collide(0, self.vel.y)

    def collide(self, xvel, yvel):
        for p in self.platforms:
            if collide_rect(self.sprite, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.collide_x = True
                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.collide_x = True
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.collide_y = True
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.collide_y = True

    def set_direction(self, dir):
        self.prev_dir = self.dir
        switcher = {
            -1: self.move_left,
            1: self.move_right,
            -2: self.move_up,
            2: self.move_down
        }
        func = switcher.get(dir, lambda: 'Invalid')
        func()

    def move_left(self):
        self.dir = -1
        self.vel.x = -1 * self.speed

    def move_right(self):
        self.dir = 1
        self.vel.x = self.speed

    def move_up(self):
        self.dir = -2
        self.vel.y = -1 * self.speed

    def move_down(self):
        self.dir = 2
        self.vel.y = self.speed

    def reset_x(self):
        self.vel.x = 0

    def reset_y(self):
        self.vel.y = 0

    def reset_dir(self):
        self.dir = self.prev_dir

    def check_teleporting(self):
        if self.rect.left <= 0 or self.rect.right >= 248:
            self.collide_y = True

        if self.rect.right <= 0:
            self.rect.left = 248
        elif self.rect.left >= 248:
            self.rect.right = 0

    def check_current_direction(self):
        if self.vel.x > 0:
            self.current_dir = 1
        elif self.vel.x < 0:
            self.current_dir = -1
        elif self.vel.y > 0:
            self.current_dir = 2
        elif self.vel.y < 0:
            self.current_dir = -2

    def check_velocity(self):
        if abs(self.dir) == 1 and self.collide_y:
            self.reset_y()
        elif abs(self.dir) == 2 and self.collide_x:
            self.reset_x()
