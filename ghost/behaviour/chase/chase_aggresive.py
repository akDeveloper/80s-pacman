from ghost.behaviour.chase.future_move import FutureMove
from ghost.behaviour.chase.chase_behaviour import ChaseBehaviour


class ChaseAggresive(ChaseBehaviour):

    def __init__(self, ghost, target):
        self.ghost = ghost
        self.target = target

    def chase(self):
        motions = self.get_available_motion_tiles()
        if self.should_take_decision(motions):
            self.take_decision(motions)

    def should_take_decision(self, motions):
        '''
        Check if a motion exists with the direction other
        than the axis that the ghost is already moving.
        '''
        for m in motions:
            if abs(m.get_direction()) != abs(self.ghost.motion.dir):
                return True

        return False

    def take_decision(self, motions):
        motions.sort(key=lambda move: move.get_distance(self.target))
        if len(motions) > 0:
            m = motions[0]
            self.ghost.motion.set_direction(m.get_direction())

    def get_available_motion_tiles(self):
        rect = self.ghost.col.rect
        s = 8  # 1 tile
        motions = []
        motions.append(FutureMove(1, rect.move(s, 0)))
        motions.append(FutureMove(-1, rect.move(-1 * s, 0)))
        motions.append(FutureMove(-2, rect.move(0, -1 * s)))
        motions.append(FutureMove(2, rect.move(0, s)))
        f = []
        for m in motions:
            if not self.collide(m.get_rect()) and \
                    not self.is_reverse_direction(m):
                f.append(m)
        return f

    def collide(self, new_rect):
        for p in self.ghost.motion.platforms:
            if new_rect.colliderect(p.rect):
                return True
        return False

    def is_reverse_direction(self, future_move):
        return future_move.get_direction() == \
                -1 * self.ghost.motion.dir
