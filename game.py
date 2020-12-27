from location import locations
from player import Player


class Game:
    def __init__(self):
        """
        Initialises the game
        """
        self.locations = locations
        self.currently = self.locations['entrance']
        self.player = Player()

    def changeLocation(self, location_name):
        if location_name in self.currently.exits:
            self.currently = self.locations[location_name]
        else:
            raise ValueError

    def addItemtoInventory(self, item):
        self.player.collect(item)

    def leaveItemAtLocation(self, item):
        self.player.leaveitem(item, self.currently)

    def getAvaialblePickUpItems(self):
        return self.currently.collectableitems

    def getAvaialbleLeaveItems(self):
        return self.currently.itemstoleave

    def getAccountBal(self):
        return self.player.money

    def getInventory(self):
        return[
            i.name for i in self.player.inventory]

    def play(self):
        """
            The main play loop
        :return: None
        """
        pass


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
