#!/usr/bin/env python3
import pygame
from game_event import GameEvent
from pygame.locals import K_ESCAPE
from game import Game


class App(GameEvent):

    FPS = 30  # 1/60th of second

    def __init__(self):
        self.__game = Game()

    def on_init(self):
        pygame.init()

    def on_loop(self):
        self.__game.update()

    def on_render(self):
        self.__game.render()

    def on_exit(self):
        self.__game.stop()

    def on_cleanup(self):
        pygame.quit()

    def on_key_down(self, event):
        self.__game.key_down(event)

    def on_key_up(self, event):
        if event.key == K_ESCAPE:
            exit()

        self.__game.key_up(event)

    def on_execute(self):
        if self.on_init() is False:
            self.__game.stop()

        clock = pygame.time.Clock()

        while(self.__game.is_running()):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            clock.tick(self.FPS)
        self.on_cleanup()


if __name__ == "__main__":
    app = App()
    app.on_execute()
