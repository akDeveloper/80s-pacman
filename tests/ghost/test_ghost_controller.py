from unittest import TestCase
from game import Game
from ghost.state import State


class TestGhostController(TestCase):
    def setUp(self):
        self.game = Game()

    def test_should_change_behaviour(self):
        controller = self.game.ghost_controller
        time = 34
        controller.control(time)
        self.assertEqual(controller.state, State.SCATTER)
        time = 7000
        controller.control(time)
        self.assertEqual(controller.state, State.CHASE)
        time = 20000
        controller.control(time)
        self.assertEqual(controller.state, State.SCATTER)
