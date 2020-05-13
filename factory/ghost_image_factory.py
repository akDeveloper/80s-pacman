from sprite_sheet import SpriteSheet


class GhostImageFactory(object):

    FILENAME = "resources/sprites/units_sprites.png"

    def __init__(self):
        self.sheet = SpriteSheet(self.FILENAME)
        self.images = []

    def create(self):
        images = [
            # Blinky
            self.sheet.get_image(1, 65, 14, 14),    # 0 Stand
            self.sheet.get_image(1, 65, 14, 14),    # 1 Right 1
            self.sheet.get_image(17, 65, 14, 14),   # 2 Right 2
            self.sheet.get_image(33, 65, 14, 14),   # 3 Left 1
            self.sheet.get_image(49, 65, 14, 14),   # 4 Left 2
            self.sheet.get_image(65, 65, 14, 14),   # 5 Up 1
            self.sheet.get_image(81, 65, 14, 14),   # 6 Up 2
            self.sheet.get_image(97, 65, 14, 14),   # 7 Down 1
            self.sheet.get_image(113, 65, 14, 14),  # 8 Down 2
            # Pinky
            self.sheet.get_image(1, 81, 14, 14),    # 9 Stand
            self.sheet.get_image(1, 81, 14, 14),    # 10 Right 1
            self.sheet.get_image(17, 81, 14, 14),   # 11 Right 2
            self.sheet.get_image(33, 81, 14, 14),   # 12 Left 1
            self.sheet.get_image(49, 81, 14, 14),   # 13 Left 2
            self.sheet.get_image(65, 81, 14, 14),   # 14 Up 1
            self.sheet.get_image(81, 81, 14, 14),   # 15 Up 2
            self.sheet.get_image(97, 81, 14, 14),   # 16 Down 1
            self.sheet.get_image(113, 81, 14, 14),  # 17 Down 2
            # Inky
            self.sheet.get_image(1, 97, 14, 14),    # 18 Stand
            self.sheet.get_image(1, 97, 14, 14),    # 19 Right 1
            self.sheet.get_image(17, 97, 14, 14),   # 20 Right 2
            self.sheet.get_image(33, 97, 14, 14),   # 21 Left 1
            self.sheet.get_image(49, 97, 14, 14),   # 22 Left 2
            self.sheet.get_image(65, 97, 14, 14),   # 23 Up 1
            self.sheet.get_image(81, 97, 14, 14),   # 24 Up 2
            self.sheet.get_image(97, 97, 14, 14),   # 25 Down 1
            self.sheet.get_image(113, 97, 14, 14),  # 26 Down 2
        ]
        for i in images:
            self.images.append(i)

    def get_image(self, index):
        return self.images[index]
