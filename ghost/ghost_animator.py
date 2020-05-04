from ghost.method_not_implemented import MethodNotImplemented


class GhostAnimator(object):
    def __init__(self, factory):
        self.factory = factory
        self.tick = 0
        self.index = 0
        self.s = self.get_sequence()

    def get_sequence(self):
        raise MethodNotImplemented("Implement `get_sequence` method")

    def next(self, dir):
        self.tick += 1
        s = self.s.get(dir)
        if self.tick > 2:
            self.index += 1
            if self.index > len(s) - 1:
                self.index = 0
            self.tick = 0
        return self.factory.get_image(s[self.index])
