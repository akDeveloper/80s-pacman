from pygame import Surface
from pygame import image


class SpriteSheet(object):

    def __init__(self, filename):
        self.sprite_sheet = image.load(filename).convert()

    def get_image(self, x, y, width, height):
        image = Surface([width, height]).convert()
        image.set_colorkey((0, 0, 0))
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        return image
