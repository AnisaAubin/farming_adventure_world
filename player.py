from items import Wheelbarrow


class Player:
    def __init__(self):
        self.inventory = []
        self.money = 0
        self.wheelbarrow = None
        self.capacity = 2

    def sell(self, item):
        self.money += item.price
        self.inventory.remove(item)
        # Remove capacity from player
        self.capacity += item.size

    def collect(self, item):
        # Allowing a player to pick up an item,
        # if they have a wheelbarrow adds item and adjusts availablecapacity.
        if isinstance(item, Wheelbarrow):
            if self.wheelbarrow is None:
                self.wheelbarrow = item
                used = sum([i.size for i in self.inventory])
                self.capacity = 6 - used
                self.inventory.append(item)
            # It's not possible to pick up a second WheelBarrow
        else:
            if item.size <= self.capacity:
                self.inventory.append(item)
                self.capacity -= item.size

    def leaveitem(self, item, location):
        # allowing player to leave item except wheelbarrow
        # if items left at the farm stall increase payout.
        if item in self.inventory:
            if location.name == "farm stall":
                self.sell(item)
            else:
                if item != self.wheelbarrow:
                    self.capacity += item.size
                    self.inventory.remove(item)
                else:
                    non_wheelbarrow_items = [
                        i for i in self.inventory if i != self.wheelbarrow]
                    # Can only leave an empty wheelbarrow
                    if non_wheelbarrow_items:
                        raise ValueError
                    else:
                        self.capacity = 2
                        self.inventory.remove(self.wheelbarrow)
                        self.wheelbarrow = None
