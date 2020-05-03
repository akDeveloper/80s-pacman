class BlinkyAnimator(object):
    def __init__(self, factory):
        self.factory = factory
        self.s = {
            0: [0],
            1: [1, 2],
            -1: [3, 4],
            -2: [5, 6],
            2: [7, 8]
        }
        self.tick = 0
        self.index = 0

    def next(self, dir):
        self.tick += 1
        s = self.s.get(dir)
        if self.tick > 2:
            self.index += 1
            if self.index > len(s) - 1:
                self.index = 0
            self.tick = 0
        return self.factory.get_image(s[self.index])
