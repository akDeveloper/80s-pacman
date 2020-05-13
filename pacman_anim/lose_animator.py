class LoseAnimator(object):
    def __init__(self, factory):
        self.factory = factory
        self.s = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.tick = 0
        self.index = 1

    def next(self):
        self.tick += 1
        s = self.s
        index = self.get_next_valid_index(s)
        if self.tick > 5:
            self.index = index
            self.tick = 0
        return self.factory.get_image(s[self.index])

    def get_next_valid_index(self, s):
        index = self.index + 1
        if index > len(s) - 1:
            index = 0
        return index

    def ended(self):
        return self.index == len(self.s) - 1
