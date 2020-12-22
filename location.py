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
        collectableitems=[Manure()]),
    'garden': Location(
        "garden",
        exits=['farm_stall', 'barn', 'rose_garden'],
        collectableitems=[Vegetables(), Herbs()],
        itemstoleave=[Water(), Manure(), Seeds()]),
    'barn': Location(
        "barn",
        exits=['chicken_coop'],
        collectableitems=[Water(), Feed(), Seeds()],
        itemstoleave=[Water(), Feed(), Seeds(), Vegetables(), Herbs()]),
    'garage': Location(
        "garage",
        exits=['workshop']),
    'workshop': Location(
        "workshop",
        exits=['garden'],
        collectableitems=[Wheelbarrow()],
        itemstoleave=[Wheelbarrow()]),
    'chicken_coop': Location(
        "chicken_coop",
        exits=['farm_stall', 'garden'],
        collectableitems=[Eggs()],
        itemstoleave=[Water(), Feed()]),
    'greenhouse': Location(
        "greenhouse",
        exits=['garden'],
        collectableitems=[Vegetables(), Herbs()],
        itemstoleave=[Water(), Manure(), Seeds()]),
    'rose_garden': Location(
        "rose_garden",
        exits=['garden'],
        collectableitems=[Roses()],
        itemstoleave=[Water(), Manure()]),
    'farm_stall': Location(
        "farm_stall",
        exits=['field'],
        itemstoleave=[Eggs(), Vegetables(), Roses(), Herbs()])
}
