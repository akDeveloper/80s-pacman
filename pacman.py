from pygame.sprite import Sprite
from entity import Entity
from motion import Motion
from factory.pacman_image_factory import PacmanImageFactory
from pacman_animator import PacmanAnimator
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame.sprite import spritecollide


class Pacman(Sprite):
    def __init__(self, pos, platforms, dots, *groups):
        super().__init__(*groups)
        self.factory = PacmanImageFactory()
        self.factory.create()
        self.animator = PacmanAnimator(self.factory)
        self.image = self.animator.next(0)
        self.rect = self.image.get_rect(center=pos)
        self.col = Entity(self.rect.x+2, self.rect.y+2, 8, 8, (255, 0, 0))
        self.speed = 2
        self.motion = Motion(self.col, self.speed, platforms)
        self.motion.set_direction(-1)
        self.dots = dots

    def update(self, key):
        self.check_user_input(key)

        '''
        Update pacman position
        '''
        self.motion.update()
        self.rect.center = self.col.rect.center
        self.eat_dots()
        '''
        x = (right / 8)
        y = (bottom / 8) - 3
        t = ((y - 1) * 28) + x
        '''
        '''
        Reset velocity and direction when
        pacman collides for the new user
        input direction
        '''
        if self.motion.collide_x:
            self.motion.reset_x()
            self.motion.reset_dir()
        if self.motion.collide_y or self.motion.teleporting:
            self.motion.reset_y()
            self.motion.reset_dir()

        '''
        Check where pacman is facing and draw sprite image
        '''
        self.motion.check_current_direction()
        if not self.motion.is_stopped():
            self.image = self.animator.next(self.motion.current_dir)

    def eat_dots(self):
        dots = spritecollide(self.col, self.dots, True)
        pass

    def move_left(self):
        self.motion.set_direction(-1)

    def move_right(self):
        self.motion.set_direction(1)

    def move_up(self):
        self.motion.set_direction(-2)

    def move_down(self):
        self.motion.set_direction(2)

    def check_user_input(self, key):
        dir = self.motion.dir
        '''
        Check user input for direction
        '''
        if (key[K_UP]):
            dir = -2
        if (key[K_RIGHT]):
            dir = 1
        if (key[K_DOWN]):
            dir = 2
        if (key[K_LEFT]):
            dir = -1
        self.motion.set_direction(dir)
