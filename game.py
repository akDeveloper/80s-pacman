import pygame
from pygame.sprite import Group
from pacman import Pacman
from level_builder import LevelBuilder
from ghost.blinky import Blinky
from pygame import Surface


class Game:

    SCREEN_WIDTH = 224
    SCREEN_HEIGHT = 288

    def __init__(self):
        self.running = True
        self.screen_size = (self.SCREEN_WIDTH * 2, self.SCREEN_HEIGHT * 2)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.sprites = Group()
        self.builder = LevelBuilder(
            "resources/levels/level1-layers.json",
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        )
        self.builder.build()
        self.player = Pacman(
            (112, 212),
            self.builder.get_platforms(),
            self.sprites
        )

        Blinky(self.sprites)

    def update(self):
        self.player.update()

    def render(self):
        # Create surface for handling graphics
        surface = Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        # Draw sprites to surface
        self.builder.get_platforms().draw(surface)
        # self.builder.get_images().draw(surface)
        surface.blit(self.builder.get_background(), (0, 0))
        self.sprites.draw(surface)

        # Copy surface to screen surface
        pygame.transform.scale(surface, self.screen_size, self.screen)
        self.screen.convert()
        pygame.display.update()

    def stop(self):
        self.running = False

    def key_down(self, e):
        if e.key == pygame.K_RIGHT:
            self.player.move_right()
        if e.key == pygame.K_LEFT:
            self.player.move_left()
        if e.key == pygame.K_UP:
            self.player.move_up()
        if e.key == pygame.K_DOWN:
            self.player.move_down()

    def key_up(self, e):
        if ((e.key == pygame.K_RIGHT) or (e.key == pygame.K_LEFT)) \
                and self.player.motion.collide_x:
            self.player.reset_x()
        if ((e.key == pygame.K_UP) or (e.key == pygame.K_DOWN)) \
                and self.player.motion.collide_y:
            self.player.reset_y()

    def is_running(self):
        return self.running
