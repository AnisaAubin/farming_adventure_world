from game import Game
from player import Player
from items import Wheelbarrow, Eggs, Vegetables, Herbs
from location import locations

import unittest

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
        # test pick up vegetables, check availbable first
        self.assertEqual(
            self.game.getAvaialblePickUpItems(), ['vegetables', 'herbs'])
        self.game.addItemtoInventory(Vegetables())
        self.assertEqual(
            self.game.getInventory(), ['Vegetables'])

    # test Selling item, inventory changing and balance.
    def test_balance(self):
        test_eggs = Eggs()  # Create instance of eggs to use
        self.assertEqual(self.game.getAccountBal(), 0)  # check starting balance
        self.game.changeLocation('barn')  # valid move
        self.game.changeLocation('chicken_coop')
        self.game.addItemtoInventory(test_eggs)  #  pick up eggs
        self.assertEqual(
            self.game.getInventory(), ['Eggs'])
        self.game.changeLocation('farm_stall')
        self.game.leaveItemAtLocation(test_eggs)  # sell eggs
        self.assertEqual(self.game.getAccountBal(), 2)
        self.assertEqual(
            self.game.getInventory(), [])


    def tearDown(self):
        del(self.game)