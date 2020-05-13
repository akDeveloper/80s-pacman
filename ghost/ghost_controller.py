from ghost.state import State


class GhostController(object):

    def __init__(self, ghosts):
        self.msec = 0
        self.interval = 0
        self.ghosts = ghosts
        self.state = State.SCATTER
        self.period = 0
        self.states = [
            [7000, State.SCATTER],
            [20000, State.CHASE],
            [7000, State.SCATTER],
            [20000, State.CHASE],
            [5000, State.SCATTER],
            [20000, State.CHASE],
            [5000, State.SCATTER],
            [20000, State.CHASE],
        ]
        self.states.reverse()

    def reset_timer(self):
        self.msec = 0

    def control(self, time):
        self.msec += time
        if (len(self.states) == 0):
            return
        if self.msec >= self.interval:
            state = self.states.pop()
            self.interval = state[0]
            self.state = state[1]
            self.change_state()
            self.period += 1
            self.reset_timer()

    def change_state(self):
        for g in self.ghosts.sprites():
            g.set_state(self.state)
