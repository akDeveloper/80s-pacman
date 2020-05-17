from ghost.ghost_animator import GhostAnimator


class PinkyAnimator(GhostAnimator):
    def get_sequence(self):
        return {
            0: [9, 9],
            1: [10, 11],
            -1: [12, 13],
            -2: [14, 15],
            2: [16, 17]
        }
