from pygame.math import Vector2


class FutureMove(object):
    TILE_WIDTH = 8

    def __init__(self, dir, rect, target):
        p = {
            -2: 0,
            -1: 1,
            2: 2,
            1: 3
        }
        self.dir = dir
        self.priority = p.get(dir)
        self.rect = rect
        self.distance = self.calculate_distance(self.get_delta_vector(target))

    def get_direction(self):
        return self.dir

    def get_rect(self):
        return self.rect

    def get_distance(self):
        return self.distance

    def get_delta_vector(self, target):
        dX = (self.rect.x - target.x) / self.TILE_WIDTH
        dY = (self.rect.y - target.y) / self.TILE_WIDTH

        return Vector2(dX, dY)

    def calculate_distance(self, vector):
        return vector.x**2 + vector.y**2
