from ghost.behaviour.chase.future_move import FutureMove
from ghost.behaviour.chase.chase_behaviour import ChaseBehaviour
from pygame import Rect


class ChaseAggresive(ChaseBehaviour):

    def __init__(self, ghost, pacman):
        self.ghost = ghost
        self.pacman = pacman

    def chase(self):
        motions = self.get_available_motion_tiles()
        motions.sort(key=lambda move: move.get_distance(self.pacman.rect))
        m = motions[0]
        self.ghost.motion.set_direction(m.get_direction())

    def get_available_motion_tiles(self):
        r = self.ghost.rect
        motions = []
        motions.append(FutureMove(1, Rect(r.x + 1, r.y, r.width, r.height)))
        motions.append(FutureMove(-1, Rect(r.x - 1, r.y, r.width, r.height)))
        motions.append(FutureMove(-2, Rect(r.x, r.y - 1, r.width, r.height)))
        motions.append(FutureMove(2, Rect(r.x, r.y + 1, r.width, r.height)))
        f = []
        for m in motions:
            if not self.check_collide(m.get_rect()):
                f.append(m)
        return f

    def check_collide(self, new_rect):
        for p in self.ghost.motion.platforms:
            if new_rect.colliderect(p.rect):
                return True
        return False
