from ghost.ghost import Ghost


class Blinky(Ghost):
    def __init__(self, *groups):
        x = 108
        y = 112
        super().__init__(x,  y, 8, 8, (255, 0, 0), *groups)

    def get_name(self):
        return "Blinky"
