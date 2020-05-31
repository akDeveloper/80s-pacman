from pygame.math import Vector2
from pygame.sprite import collide_rect
from door import Door


class Motion(object):
    UP = -2
    DOWN = 2
    LEFT = -1
    RIGHT = 1
    X_AXIS = 1
    Y_AXIS = 2

    def __init__(self, sprite, speed, platforms):
        self.speed = speed
        self.dir = 0  # The direction from input
        self.current_dir = 0  # The actual direction of sprite
        self.prev_dir = 0  # The previous direction to restore
        self.vel = Vector2(0, 0)
        self.platforms = platforms
        self.rect = sprite.rect
        self.sprite = sprite
        self.collide_x = False
        self.collide_y = False
        self.delta = Vector2(0, 0)
        self.teleporting = False

    def update(self, skip_door: bool = False):
        self.check_teleporting()
        self.check_x_axis_collide(skip_door)
        self.check_y_axis_collide(skip_door)
        self.check_velocity()

    def check_x_axis_collide(self, skip_door: bool):
        self.rect.left += self.vel.x
        self.delta.x = self.vel.x
        self.collide_x = False
        self.collide(self.vel.x, 0, skip_door)

    def check_y_axis_collide(self, skip_door: bool):
        if not self.teleporting:
            self.rect.top += self.vel.y
            self.delta.y = self.vel.y
        self.collide_y = False
        self.collide(0, self.vel.y, skip_door)

    def collide(self, xvel: int, yvel: int, skip_door: bool):
        for p in self.platforms:
            if skip_door is True and isinstance(p, Door):
                continue
            if collide_rect(self.sprite, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.collide_x = True
                    self.delta.x = 0
                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.collide_x = True
                    self.delta.x = 0
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.collide_y = True
                    self.delta.y = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.collide_y = True
                    self.delta.y = 0

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

    def is_stopped(self):
        if self.delta.x == 0 and self.delta.y == 0:
            return True
        return False

    def move_left(self):
        self.dir = self.LEFT
        self.vel.x = -1 * self.speed

    def move_right(self):
        self.dir = self.RIGHT
        self.vel.x = self.speed

    def move_up(self):
        self.dir = self.UP
        self.vel.y = -1 * self.speed

    def move_down(self):
        self.dir = self.DOWN
        self.vel.y = self.speed

    def reset_x(self):
        self.vel.x = 0

    def reset_y(self):
        self.vel.y = 0

    def reset_dir(self):
        self.dir = self.prev_dir

    def should_move_to_x(self):
        return abs(self.dir) == 1

    def should_move_to_y(self):
        return abs(self.dir) == 2

    def check_teleporting(self):
        if self.rect.left <= 2 or self.rect.right >= 222:
            self.teleporting = True
        else:
            self.teleporting = False

        if self.rect.right <= 0:
            self.rect.left = 248
        elif self.rect.left >= 248:
            self.rect.right = 0

    def check_current_direction(self):
        if self.delta.x != 0:
            self.current_dir = int(self.delta.x / self.speed)
        elif self.delta.y != 0:
            self.current_dir = int((self.delta.y / self.speed) * 2)
        else:
            self.current_dir = 0

    def check_velocity(self):
        if abs(self.dir) == self.X_AXIS and self.collide_y:
            self.reset_y()
        elif abs(self.dir) == self.Y_AXIS and self.collide_x:
            self.reset_x()
