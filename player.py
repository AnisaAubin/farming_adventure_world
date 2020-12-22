from items import Wheelbarrow


class Player:
    def __init__(self):
        self.inventory = []
        self.money = 0
        self.wheelbarrow = None
        self._capacity = 2

    def sell(self, item):
        self.money += item.price
        self.inventory.remove(item)
        # Remove capacity from player (or wheelbarrow if they have one)
        if self.wheelbarrow is not None:
            self.wheelbarrow.removeitem(item)
        else:
            self._capacity += item.size

    @property
    # sets the players carrying capacity to 2 if they don't have the
    # wheelbarrow otherwise the wheelbarrows.
    def capacity(self):
        if self.wheelbarrow is not None:
            return self.wheelbarrow.availableCapacity
        else:
            return self._capacity

    def collect(self, item):
        # Allowing a player to pick up an item,
        # if they have a wheelbarrow adds item and adjusts availablecapacity.
        if isinstance(item, Wheelbarrow):
            if self.wheelbarrow is not None:
                pass  # don't let player pick up a duplicated wheelbarrow.
            else:
                self.wheelbarrow = item
                for i in self.inventory:
                    self.wheelbarrow.additem(i)  # + current items to barrow
                self.inventory.append(item)
        else:
            if item.size < self.capacity:
                self.inventory.append(item)
                if self.wheelbarrow is not None:
                    self.wheelbarrow.additem(item)
                else:
                    self._capacity -= item.size

    def leaveitem(self, item, location):
        # allowing player to leave item except wheelbarrow
        # if items left at the farm stall increase payout.
        if item in self.inventory:
            if location.name == "farm stall":
                self.sell(item)
            else:
                if item != self.wheelbarrow:
                    self._capacity += item.size
                    self.inventory.remove(item)
                else:
                    non_wheelbarrows = [
                        i for i in self.inventory if i != self.wheelbarrow]
                    # Can only leave an empty wheelbarrow
                    if non_wheelbarrows:
                        raise ValueError
                    else:
                        self._capacity = 2
                        self.inventory.remove(self.wheelbarrow)
                        self.wheelbarrow = None
