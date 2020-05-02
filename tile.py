from entity import Entity


class Tile(Entity):
    COLOR = (60, 137, 200)

    def __init__(self, x, y, *groups):
        w = 8
        h = 8
        super().__init__(x, y, w, h, self.COLOR, *groups)

    def set_image(self, image):
        self.image = image
