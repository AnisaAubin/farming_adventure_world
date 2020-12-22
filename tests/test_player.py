from player import Player
from items import Wheelbarrow, Eggs
from location import locations

import unittest


# test that adding item without wheelbarrow.
class TestGame(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_player_add_Wheelbarrow(self):
        self.assertEqual(self.player.capacity, 2)
        self.wheelbarrow = Wheelbarrow()
        self.player.collect(self.wheelbarrow)
        self.assertEqual(self.player.capacity, 6)

    def test_player_add_eggs_to_Wheelbarrow(self):
        self.assertEqual(self.player.capacity, 2)
        self.player.collect(Eggs())
        self.assertEqual(self.player.capacity, 1)
        self.wheelbarrow = Wheelbarrow()
        self.player.collect(self.wheelbarrow)
        self.assertEqual(self.player.capacity, 5)
        # ValueError, wheelbarrow not left because it holds eggs
        self.assertRaises(
            ValueError,
            self.player.leaveitem, self.wheelbarrow, locations['garden'])
        self.assertEqual(self.player.capacity, 5)

    def tearDown(self):
        del(self.player)
