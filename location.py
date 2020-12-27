from items import (
    Manure, Vegetables, Eggs, Water,  Feed, Seeds, Herbs, Wheelbarrow, Roses
)
"""
    Create locations described "description". Initially, it has
    no exits. 'description' is something like 'kitchen' or
    'an open court yard'
"""


class Location:
    def __init__(
            self, name, exits,
            collectableitems=None, itemstoleave=None):
        """
            Constructor method
        :param description: text description for this location
        """
        self.name = name
        self.description = f"In the {self.name}"
        self.exits = exits
        self.collectableitems = collectableitems or []
        self.itemstoleave = itemstoleave or []


locations = {
    'entrance': Location(
        "entrance",
        exits=['garden', 'field', 'garage', 'barn']),
    'field': Location(
        "field",
        exits=['garden'],
        collectableitems=["manure", "honey"]),
    'garden': Location(
        "garden",
        exits=['farm_stall', 'barn', 'rose_garden', 'greenhouse'],
        collectableitems=["vegetables", "herbs"],
        itemstoleave=["water", "manure", "seeds"]),
    'barn': Location(
        "barn",
        exits=['chicken_coop'],
        collectableitems=["water", "feed", "seeds"],
        itemstoleave=["water", "feed", "seeds", "vegetables", "herbs"]),
    'garage': Location(
        "garage",
        exits=['workshop']),
    'workshop': Location(
        "workshop",
        exits=['garden'],
        collectableitems=["wheelbarrow"],
        itemstoleave=["wheelbarrow"]),
    'chicken_coop': Location(
        "chicken_coop",
        exits=['farm_stall', 'garden'],
        collectableitems=["eggs"],
        itemstoleave=["water", "feed"]),
    'greenhouse': Location(
        "greenhouse",
        exits=['garden'],
        collectableitems=["vegetables", "herbs"],
        itemstoleave=["water", "manure", "seeds"]),
    'rose_garden': Location(
        "rose_garden",
        exits=['garden'],
        collectableitems=["roses"],
        itemstoleave=["water", "manure"]),
    'farm_stall': Location(
        "farm_stall",
        exits=['field'],
        itemstoleave=["eggs", "vegetables", "roses", "herbs", "honey"])
}
