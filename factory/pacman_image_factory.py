from sprite_sheet import SpriteSheet


class PacmanImageFactory(object):

    FILENAME = "resources/sprites/units_sprites.png"

    def __init__(self):
        self.sheet = SpriteSheet(self.FILENAME)
        self.images = []

    def create(self):
        self.images.append(
            self.sheet.get_image(33, 1, 13, 13)
        )

    def get_image(self, index):
        return self.images[index]
