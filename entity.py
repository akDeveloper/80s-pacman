from pygame.sprite import Sprite
from pygame import Surface
import pygame
from pygame import Rect


class Entity(Sprite):
    def __init__(self, x, y, w, h, color, *groups):
        super().__init__(*groups)
        self.image = Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        pygame.draw.rect(self.image, (100, 100, 100), Rect(0, 0, w, h), 1)
