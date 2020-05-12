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
            self.sheet.get_image(17, 17, 13, 13),  # Left 1
            self.sheet.get_image(1, 17, 13, 13),  # Left 2
            self.sheet.get_image(17, 33, 13, 13),  # Up 1
            self.sheet.get_image(1, 33, 13, 13),  # Up 2
            self.sheet.get_image(17, 49, 13, 13),  # Down 1
            self.sheet.get_image(1, 49, 13, 13),  # Down 2

            self.sheet.get_image(49, 0, 13, 13),  # Death
            self.sheet.get_image(64, 0, 15, 13),  # Death
            self.sheet.get_image(80, 0, 15, 13),  # Death
            self.sheet.get_image(96, 0, 15, 13),  # Death
            self.sheet.get_image(112, 0, 15, 13),  # Death
            self.sheet.get_image(128, 0, 15, 13),  # Death
            self.sheet.get_image(144, 2, 15, 13),  # Death
            self.sheet.get_image(160, 2, 15, 13),  # Death
            self.sheet.get_image(176, 2, 13, 13),  # Death
            self.sheet.get_image(192, 0, 13, 13),  # Death
            self.sheet.get_image(208, 3, 13, 13),  # Death
        ]
        for i in images:
            self.images.append(i)

    def get_image(self, index):
        return self.images[index]
