from ghost.ghost_animator import GhostAnimator


class BlinkyAnimator(GhostAnimator):
    def get_sequence(self):
        return {
            0: [0, 0],
            1: [1, 2],
            -1: [3, 4],
            -2: [5, 6],
            2: [7, 8]
        }
