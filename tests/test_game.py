from game import Game
from player import Player
from items import Wheelbarrow, Eggs, Vegetables, Herbs
from location import locations

import unittest


# test that adding item without wheelbarrow.
class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_play_game(self):
        self.assertEqual(self.game.currently.name, 'entrance')
        # print(self.game.locations)
        self.game.changeLocation('garden')
        self.assertEqual(self.game.currently.name, 'garden')
        #  try go to an invalid location
        self.assertRaises(
            ValueError, self.game.changeLocation, 'entrance'
        )
        #self.assertEqual(
            #self.game.getAvaialblePickUpItems(), [Vegetables(), Herbs()])
        
    def test_balance(self):
        self.assertEqual(self.game.getAccountBal(), 0)

    def tearDown(self):
        del(self.game)