from ghost.ghost_animator import GhostAnimator


class InkyAnimator(GhostAnimator):
    def get_sequence(self):
        return {
            0: [18],
            1: [19, 20],
            -1: [21, 22],
            -2: [23, 24],
            2: [25, 26]
        }
