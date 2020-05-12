class WalkAnimator(object):
    def __init__(self, factory):
        self.factory = factory
        self.s = {
            0: [0],
            1: [0, 1, 2],
            -1: [0, 3, 4],
            -2: [0, 5, 6],
            2: [0, 7, 8]
        }
        self.tick = 0
        self.index = 0
        self.fast = 0
        self.slow = 1

    def next(self, dir):
        self.tick += 1
        s = self.s.get(dir)
        index = self.get_next_valid_index(s)
        time = self.slow
        if (index == 0):
            time = self.fast
        if self.tick > time:
            self.increase_index(index)
            self.tick = 0
        return self.factory.get_image(s[self.index])

    def get_next_valid_index(self, s):
        index = self.index + 1
        if index > len(s) - 1:
            index = 0
        return index

    def increase_index(self, index):
        self.index = index
