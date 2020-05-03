from sprite_sheet import SpriteSheet


class PacmanImageFactory(object):

    FILENAME = "resources/sprites/units_sprites.png"

    def __init__(self):
        self.sheet = SpriteSheet(self.FILENAME)
        self.images = []

    def create(self):
        images = [
            self.sheet.get_image(33, 1, 13, 13),  # Stand
            self.sheet.get_image(17, 1, 13, 13),  # Right 1
            self.sheet.get_image(1, 1, 13, 13),  # Right 2
            self.sheet.get_image(18, 17, 13, 13),  # Left 1
            self.sheet.get_image(2, 17, 13, 13),  # Left 2
            self.sheet.get_image(17, 33, 13, 13),  # Up 1
            self.sheet.get_image(1, 33, 13, 13),  # Up 2
            self.sheet.get_image(17, 48, 13, 13),  # Down 1
            self.sheet.get_image(1, 48, 13, 13),  # Down 2
        ]
        for i in images:
            self.images.append(i)

    def get_image(self, index):
        return self.images[index]
