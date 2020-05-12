from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame.key import get_pressed


class PacmanInput(object):

    def get_direction(self, dir):
        key = get_pressed()
        if (key[K_UP]):
            dir = -2
        if (key[K_RIGHT]):
            dir = 1
        if (key[K_DOWN]):
            dir = 2
        if (key[K_LEFT]):
            dir = -1
        return dir
