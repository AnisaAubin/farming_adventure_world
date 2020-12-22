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
