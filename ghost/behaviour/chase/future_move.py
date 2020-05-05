from pygame.math import Vector2


class FutureMove(object):
    def __init__(self, dir, rect):
        self.dir = dir
        self.rect = rect
        self.distance = None

    def get_direction(self):
        return self.dir

    def get_rect(self):
        return self.rect

    def get_distance(self, target):
        self.distance = self.calculate_distance(self.get_delta_vector(target))
        return self.distance

    def get_delta_vector(self, target):
        dX = self.rect.x - target.x
        dY = self.rect.y - target.y

        return Vector2(dX, dY)

    def calculate_distance(self, vector):
        return (vector.x * vector.x) + (vector.y * vector.y)
