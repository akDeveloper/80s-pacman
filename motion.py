from pygame.math import Vector2
from pygame.sprite import collide_rect


class Motion(object):
    def __init__(self, sprite, speed, platforms):
        self.speed = speed
        self.dir = 0
        self.vel = Vector2(0, 0)
        self.platforms = platforms
        self.rect = sprite.rect
        self.sprite = sprite

    def update(self):
        self.rect.left += self.vel.x
        self.collide_x = False
        self.collide(self.vel.x, 0)

        self.rect.top += self.vel.y
        self.collide_y = False
        self.collide(0, self.vel.y)

        if (self.dir == -1 or self.dir == 1) and self.collide_y:
            self.vel.y = 0
        elif (self.dir == -2 or self.dir == 2) and self.collide_x:
            self.vel.x = 0

        if self.rect.right < 0:
            self.dir = 1
            self.rect.left = 248
        elif self.rect.left > 248:
            self.dir = -1
            self.rect.right = 0

    def collide(self, xvel, yvel):
        for p in self.platforms:
            if collide_rect(self.sprite, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.collide_x = True
                    self.collide_y = False
                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.collide_x = True
                    self.collide_y = False
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.collide_y = True
                    self.collide_x = False
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.collide_y = True
                    self.collide_x = False

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
