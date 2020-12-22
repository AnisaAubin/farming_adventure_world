from abc import abstractproperty


class Item:
    @abstractproperty
    def size(self):
        pass


class Seeds(Item):
    @property
    def size(self):
        return 3


class Water(Item):
    @property
    def size(self):
        return 3


class Feed(Item):
    @property
    def size(self):
        return 2


class Manure(Item):
    @property
    def size(self):
        return 5


class Wheelbarrow(Item):
    @property
    def size(self):
        return 7  # size too big to put in the wheelbarrow.

    def __init__(self):
        self.capacity = 6  # the items in the wheelbarrow cannot exceed this.
        self.items = []  # what is in the wheelbarrow
        self.availableCapacity = 6  # remaining space in wheelbarrow

    def additem(self, item):
        # check if item can fit in wheelbarrow and adjust capacity
        if item.size <= self.availableCapacity:
            self.items.append(item)
            self.availableCapacity -= item.size
        else:
            raise ValueError

    def removeitem(self, item):
        if item in self.items:
            self.items.remove(item)
            self.availableCapacity += item.size
        else:
            raise IndexError


class SellableItem(Item):
    @abstractproperty
    def price(self):
        pass


class Eggs(SellableItem):
    @property
    def size(self):
        return 1

    @property
    def price(self):
        return 2


class Vegetables(SellableItem):
    @property
    def size(self):
        return 2

    @property
    def price(self):
        return 3


class Herbs(SellableItem):
    @property
    def size(self):
        return 1

    @property
    def price(self):
        return 4


class Roses(SellableItem):
    @property
    def size(self):
        return 1

    @property
    def price(self):
        return 5
