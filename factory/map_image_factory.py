from sprite_sheet import SpriteSheet


class MapImageFactory(object):
    FILENAME = "resources/sprites/map_sprites.png"

    def __init__(self):
        self.sheet = SpriteSheet(self.FILENAME)
        self.images = []

    def create(self):
        x_off = 1
        y_off = 1
        x = 0
        y = 0
        for i in range(143):
            self.images.append(
                self.sheet.get_image(
                    (x * 8) + (x_off), (y * 8) + (y_off), 8, 8
                )
            )
            x += 1
            x_off += 1
            if x > 15:
                x = 0
                x_off = 1
                y += 1
                y_off += 1

    def get_image(self, index):
        return self.images[index - 2]
