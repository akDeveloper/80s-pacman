from pygame.sprite import Sprite
from pygame import Surface


class Entity(Sprite):
    def __init__(self, x, y, w, h, color, *groups):
        super().__init__(*groups)
        self.image = Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
