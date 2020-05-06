from ghost.behaviour.future_move import FutureMove
from pygame import Rect


class TargetLocator(object):
    def __init__(self, ghost, target, allow_reverse=False):
        self.ghost = ghost
        self.target = target
        self.old_direction = ghost.motion.dir
        self.allow_reverse = allow_reverse
        self.red_areas = [
            Rect(88, 112, 48, 8),
            Rect(88, 208, 48, 8)
        ]

    def get_direction(self):
        motions = self.get_available_motion_tiles()
        if self.should_take_decision(motions):
            return self.take_decision(motions)
        return self.old_direction

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
        motions.sort(key=lambda move: move.get_distance())
        if self.are_distance_equal(motions):
            motions.sort(key=lambda move: move.priority)
        if len(motions) > 0:
            m = motions[0]
            return m.get_direction()
        return self.old_direction

    def get_available_motion_tiles(self):
        rect = self.ghost.col.rect
        s = 8  # 1 tile
        motions = []
        motions.append(FutureMove(1, rect.move(s, 0), self.target))
        motions.append(FutureMove(-1, rect.move(-1 * s, 0), self.target))
        motions.append(FutureMove(-2, rect.move(0, -1 * s), self.target))
        motions.append(FutureMove(2, rect.move(0, s), self.target))

        f = list(filter(self.not_collide, motions))
        if (self.allow_reverse is False):
            f = list(filter(self.is_not_reverse_direction, f))
        f = list(filter(self.not_in_red_areas, f))
        return f

    def not_collide(self, m):
        for p in self.ghost.motion.platforms:
            if m.get_rect().colliderect(p.rect):
                return False
        return True

    def is_not_reverse_direction(self, future_move):
        return not (future_move.get_direction() == -1 * self.ghost.motion.dir)

    def not_in_red_areas(self, m):
        for a in self.red_areas:
            if self.ghost.col.rect.colliderect(a) \
                    and m.get_direction() == -2:
                return False
        return True

    def are_distance_equal(self, motions):
        result = list(map(lambda m: m.get_distance(), motions))
        return len(set(result)) == 1
