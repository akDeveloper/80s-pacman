from pygame.sprite import Sprite
from entity import Entity
from motion import Motion
from factory.pacman_image_factory import PacmanImageFactory
from pacman_anim.death_animator import DeathAnimator
from pacman_anim.walk_animator import WalkAnimator
from pygame.sprite import spritecollide
from pygame.sprite import collide_rect
from energizer import Energizer
from pygame.mixer import Sound


class Pacman(Sprite):
    def __init__(self, pos, platforms, dots, ghosts, *groups):
        super().__init__(*groups)
        self.factory = PacmanImageFactory()
        self.factory.create()
        self.animator = WalkAnimator(self.factory)
        self.death_animator = DeathAnimator(self.factory)
        self.image = self.animator.next(0)
        self.rect = self.image.get_rect(center=pos)
        self.col = Entity(self.rect.x+2, self.rect.y+2, 8, 8, (255, 0, 0))
        self.speed = 2
        self.motion = Motion(self.col, self.speed, platforms)
        self.motion.set_direction(Motion.LEFT)
        self.dots = dots
        self.alive = True
        self.ghosts = ghosts
        self.munch1 = Sound('resources/sounds/munch_1.wav')
        self.munch2 = Sound('resources/sounds/munch_2.wav')
        self.death_sound = Sound('resources/sounds/death_1.wav')
        self.current_munch = 2

    def update(self, time):
        self.check_ghost_collide()
        if self.alive:
            self.move(time)
        else:
            self.dead()

    def move(self, time):
        '''
        Update pacman position
        '''
        self.motion.update()
        self.rect.center = self.col.rect.center
        self.eat_dots(time)
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

    def dead(self):
        self.image = self.death_animator.next()

    def death_completed(self):
        return self.death_animator.ended()

    def eat_dots(self, time):
        dots = spritecollide(self.col, self.dots, True)
        if (len(dots) > 0):
            if self.current_munch == 1:
                self.munch1.play()
                self.current_munch = 2
            else:
                self.munch2.play()
                self.current_munch = 1
            dot = dots[0]
            if isinstance(dot, Energizer):
                print("BIG!!!!")
        pass

    def set_direction(self, dir):
        self.motion.set_direction(dir)

    def check_ghost_collide(self):
        if not self.alive:
            return
        for g in self.ghosts:
            if collide_rect(self.col, g.col):
                self.alive = False
                self.death_sound.play()
                return

    def kill(self):
        self.col.kill()
        super().kill()
