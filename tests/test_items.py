import unittest
from items import Manure, Wheelbarrow, Water


class TestGame(unittest.TestCase):
    def setUp(self):
        self.wheelbarrow = Wheelbarrow()

    def test_additem(self):
        currentcapacity = self.wheelbarrow.availableCapacity
        water = Water()
        self.wheelbarrow.additem(water)
        self.assertEqual(
            self.wheelbarrow.availableCapacity,
            currentcapacity - water.size)
        self.assertIn(water, self.wheelbarrow.items)

    def test_overcapacity(self):
        manure = Manure()
        self.wheelbarrow.additem(manure)
        self.assertIn(manure, self.wheelbarrow.items)
        self.assertRaises(
            ValueError, self.wheelbarrow.additem, Water())

    def test_removeitem(self):
        water = Water()
        original_capacity = self.wheelbarrow.availableCapacity
        self.wheelbarrow.additem(water)
        self.assertIn(water, self.wheelbarrow.items)
        self.wheelbarrow.removeitem(water)
        self.assertEqual(self.wheelbarrow.items, [])
        self.assertEqual(self.wheelbarrow.capacity, original_capacity)

    def tearDown(self):
        del(self.wheelbarrow)


if __name__ == "__main__":
    unittest.main()
