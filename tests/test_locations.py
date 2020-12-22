from location import locations

import unittest


# test that all exist listed are valid locations.
class TestGame(unittest.TestCase):
    def test_locations_connectivity_is_valid(self):
        for location in locations.values():
            for exit in location.exits:
                self.assertIn(exit, locations.keys())
