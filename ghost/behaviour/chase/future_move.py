from pygame.math import Vector2


class FutureMove(object):
    def __init__(self, dir, rect):
        self.dir = dir
        self.rect = rect

    def get_direction(self):
        return self.dir

    def get_rect(self):
        return self.rect

    def get_distance(self, pacman):
        return self.calculate_distance(self.get_delta_vector(pacman))

    def get_delta_vector(self, pacman):
        dX = self.rect.x - pacman.x
        dY = self.rect.y - pacman.y

        return Vector2(dX, dY)

    def calculate_distance(self, vector):
        return (vector.x * vector.x) + (vector.y * vector.y)
