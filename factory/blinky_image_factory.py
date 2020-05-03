from sprite_sheet import SpriteSheet


class BlinkyImageFactory(object):

    FILENAME = "resources/sprites/units_sprites.png"

    def __init__(self):
        self.sheet = SpriteSheet(self.FILENAME)
        self.images = []

    def create(self):
        images = [
            self.sheet.get_image(1, 65, 14, 14),  # Stand
            self.sheet.get_image(1, 65, 14, 14),  # Right 1
            self.sheet.get_image(17, 65, 14, 14),  # Right 2
            self.sheet.get_image(33, 65, 14, 14),  # Left 1
            self.sheet.get_image(49, 65, 14, 14),  # Left 2
            self.sheet.get_image(65, 65, 14, 14),  # Up 1
            self.sheet.get_image(81, 65, 14, 14),  # Up 2
            self.sheet.get_image(97, 65, 14, 14),  # Down 1
            self.sheet.get_image(113, 65, 14, 14),  # Down 2
        ]
        for i in images:
            self.images.append(i)

    def get_image(self, index):
        return self.images[index]
