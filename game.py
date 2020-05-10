import pygame
from pygame.sprite import Group
from pacman import Pacman
from level_builder import LevelBuilder
from ghost.blinky.blinky import Blinky
from ghost.pinky.pinky import Pinky
from pygame import Surface
from pygame.key import get_pressed
from ghost.ghost_controller import GhostController
from pygame.locals import K_d


class Game:

    SCREEN_WIDTH = 224
    SCREEN_HEIGHT = 288

    def __init__(self):
        self.running = True
        self.event = None
        self.screen_size = (self.SCREEN_WIDTH * 2, self.SCREEN_HEIGHT * 2)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.sprites = Group()
        self.ghosts = Group()
        self.debug_group = Group()
        self.debug = False
        self.builder = LevelBuilder(
            "resources/levels/level1.json",
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        )
        self.builder.build()
        '''
        Load actors
        '''
        self.player = Pacman(
            (112, 212),
            self.builder.get_platforms(),
            self.builder.get_dots(),
            self.sprites
        )

        self.blinky = Blinky(
            self.player,
            self.builder.get_platforms(),
            self.sprites,
            self.ghosts,
            self.debug_group
        )

        self.pinky = Pinky(
            self.player,
            self.builder.get_platforms(),
            self.sprites,
            self.ghosts,
            self.debug_group
        )

        self.ghost_controller = GhostController(self.ghosts)

    def update(self, time):
        self.player.update(get_pressed())
        self.ghost_controller.control(time)
        self.ghosts.update(time)

    def render(self):
        # Create surface for handling graphics
        surface = Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Draw background to surface
        surface.blit(self.builder.get_background(), (0, 0))
        # draw dots
        self.builder.get_dots().draw(surface)

        if self.debug:
            # Draw helper platforms
            self.builder.get_platforms().draw(surface)
            self.debug_group.draw(surface)

        # Draw sprites to surface
        self.sprites.draw(surface)

        # Copy surface to screen surface
        pygame.transform.scale(surface, self.screen_size, self.screen)
        # self.screen.convert()
        pygame.display.flip()

    def stop(self):
        self.running = False

    def key_down(self, e):
        self.event = e
        if e.key == K_d:
            if self.debug == True:
                self.debug = False
            else:
                self.debug = True

    def key_up(self, e):
        self.event = e

    def is_running(self):
        return self.running
