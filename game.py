import pygame
from pygame import Surface
from pygame.locals import K_d, K_p
from level import Level


class Game:

    SCREEN_WIDTH = 224
    SCREEN_HEIGHT = 288

    def __init__(self):
        self.running = True
        self.screen_size = (self.SCREEN_WIDTH * 2, self.SCREEN_HEIGHT * 2)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.debug = False
        self.paused = False
        self.__init_level()

    def update(self, time):
        if self.paused:
            return
        self.level.update(time)

    def render(self):
        # Create surface for handling graphics
        surface = Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        if self.debug is True:
            self.level.render_debug(surface)
        else:
            self.level.render(surface)

        # Copy surface to screen surface
        pygame.transform.scale(surface, self.screen_size, self.screen)
        # self.screen.convert()
        pygame.display.flip()

    def stop(self):
        self.running = False

    def key_down(self, e):
        if e.key == K_d:
            if self.debug is True:
                self.debug = False
            else:
                self.debug = True
        if e.key == K_p:
            if self.paused is True:
                self.paused = False
            else:
                self.paused = True

    def key_up(self, e):
        pass

    def is_running(self):
        return self.running

    def __init_level(self):
        self.level = Level(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
