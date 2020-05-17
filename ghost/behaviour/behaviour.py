from ghost.method_not_implemented import MethodNotImplemented
from pygame import Rect


class Behaviour(object):

    def execute(self):
        raise MethodNotImplemented("Implement `set_state` method")

    def get_target(self) -> Rect:
        raise MethodNotImplemented("Implement `set_state` method")
