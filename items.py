from abc import abstractproperty


class Item:
    @abstractproperty
    def size(self):
        pass


class Seeds(Item):
    name = 'Seeds'
    size = 2


class Water(Item):
    name = 'Water'
    size = 3


class Feed(Item):
    name = 'Feed'
    size = 2


class Manure(Item):
    name = 'Manure'
    size = 5


class Wheelbarrow(Item):
    name = 'Wheelbarrow'
    size = 7


class SellableItem(Item):
    @abstractproperty
    def price(self):
        pass


class Eggs(SellableItem):
    name = 'Eggs'
    size = 1
    price = 2


class Vegetables(SellableItem):
    name = 'Vegetables'
    size = 2
    price = 3


class Herbs(SellableItem):
    name = 'Herbs'
    size = 1
    price = 4


class Roses(SellableItem):
    name = 'Roses'
    size = 1
    price = 5


class Honey(SellableItem):
    name = 'Honey'
    size = 1
    price = 7