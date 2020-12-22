from abc import abstractproperty


class Item:
    @abstractproperty
    def size(self):
        pass


class Seeds(Item):
    size = 3


class Water(Item):
    size = 3


class Feed(Item):
    size = 2


class Manure(Item):
    size = 5


class Wheelbarrow(Item):
    size = 7


class SellableItem(Item):
    @abstractproperty
    def price(self):
        pass


class Eggs(SellableItem):
    size = 1
    price = 2


class Vegetables(SellableItem):
    size = 2
    price = 3


class Herbs(SellableItem):
    size = 1
    price = 4


class Roses(SellableItem):
    size = 1
    price = 5
