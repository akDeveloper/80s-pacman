from ghost.behaviour.future_move import FutureMove
from pygame import Rect


class TargetLocator(object):
    def __init__(self, ghost):
        self.ghost = ghost
        self.old_direction = ghost.motion.dir
        self.allow_reverse = False
        self.red_areas = [
            Rect(88, 112, 48, 8),
            Rect(88, 208, 48, 8)
        ]

    def set_reverse(self, condition: bool) -> None:
        self.allow_reverse = condition

    def get_direction(self, target: Rect) -> int:
        motions = self.get_available_motion_tiles(target)
        if self.should_take_decision(motions):
            return self.take_decision(motions)
        return self.old_direction

    def should_take_decision(self, motions: list) -> bool:
        if self.ghost.motion.teleporting:
            return False
        '''
        Check if a motion exists with the direction other
        than the axis that the ghost is already moving.
        '''
        for m in motions:
            if abs(m.get_direction()) != abs(self.ghost.motion.dir):
                return True
        return False

    def take_decision(self, motions: list) -> int:
        self.set_reverse(False)
        self.ghost.state_changed = False
        motions.sort(key=lambda move: move.get_distance())
        if self.are_distance_equal(motions):
            motions.sort(key=lambda move: move.priority)
        if len(motions) > 0:
            m = motions[0]
            return m.get_direction()
        return self.old_direction

    def get_available_motion_tiles(self, target: Rect) -> list:
        """ target -- Rect """
        rect = self.ghost.col.rect
        s = 8  # 1 tile
        motions = []
        motions.append(FutureMove(1, rect.move(s, 0), target))
        motions.append(FutureMove(-1, rect.move(-1 * s, 0), target))
        motions.append(FutureMove(-2, rect.move(0, -1 * s), target))
        motions.append(FutureMove(2, rect.move(0, s), target))

        f = list(filter(self.not_collide, motions))
        if self.allow_reverse is False:
            f = list(filter(self.is_not_reverse_direction, f))
        f = list(filter(self.not_in_red_areas, f))
        return f

    def not_collide(self, m: FutureMove) -> bool:
        for p in self.ghost.motion.platforms:
            if m.get_rect().colliderect(p.rect):
                return False
        return True

    def is_not_reverse_direction(self, m: FutureMove):
        return not (m.get_direction() == -1 * self.ghost.motion.dir)

    def not_in_red_areas(self, m: FutureMove):
        for a in self.red_areas:
            if self.ghost.col.rect.colliderect(a) \
                    and m.get_direction() == -2:
                return False
        return True

    def are_distance_equal(self, motions: list) -> bool:
        result = list(map(lambda m: m.get_distance(), motions))
        return len(set(result)) == 1
