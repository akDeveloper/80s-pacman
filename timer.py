class Timer(object):
    def __init__(self, delay):
        self.delay = delay
        self.counter = 0

    def completed(self, time):
        self.counter += time
        if self.counter >= self.delay:
            return True
        return False

    def looped(self, time):
        self.counter += time
        if self.counter >= self.delay:
            self.counter = 0
            return True
        return False
