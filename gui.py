import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from game import Game
import random
from functools import partial
import logging

import items

logging.basicConfig(
    level=logging.INFO,
    filemode='w',  # set log to overwrite note apprend 'a', or rotation
    filename='event.log')
log = logging.getLogger(__name__)


class App(tk.Frame):
    # Creates a Frame for the application
    # and populates the GUI ...
    def __init__(self, root):

        self.game = Game()

        # Create two frames owned by the window root
        # In order to use multiple layout managers, the frames
        # cannot share a parent frame. Here both frames are owned
        # by a top level instance root.

        super().__init__(master=root)
        # set up the Gameframe
        self.gameFrame = tk.Frame(
            root, width=1025, height=550, bg='WHITE', borderwidth=3)
        self.gameFrame.grid_propagate(0)   # Prevents resizing
        self.gameFrame.columnconfigure(0, weight=0)
        self.gameFrame.columnconfigure(1, weight=4)
        self.gameFrame.columnconfigure(2, weight=0)
        self.gameFrame.pack_propagate(0)   # Prevents resizing
        self.inventoryVar = tk.StringVar(value=['Your Inventory'])  # adding variable to hold inventory in gameframe
        # set up the Navigationframe
        self.navFrame = tk.Frame(
            root, width=1025, height=550, bg='GREY', borderwidth=3)
        self.navFrame.grid_propagate(0)   # Prevents resizing
        # This packs both frames into the root window ...
        self.gameFrame.pack()
        self.navFrame.pack()

        # add buttons to the menubar
        menubar = tk.Menu()
        menubar.add_command(label='About', command=self.showAbout)
        menubar.add_command(label='Account', command=self.showAccount)
        menubar.add_command(label='Inventory', command=self.showItems)
        menubar.add_command(label='Hints', command=self.displayHint)
        menubar.add_command(label='Quit', command=root.destroy)
        # Account = tk.Menu()
        # menubar.(label="ChangeText", menu=Account)
        root.config(menu=menubar)

        # Now we add images (for NavFrame). These are stored in the images/ folder
        self.ghsImg = ImageTk.PhotoImage(Image.open('images/greenhouse.png')) 
        self.rsegdnImg = ImageTk.PhotoImage(Image.open('images/rose_garden.png'))
        self.gdnImg = ImageTk.PhotoImage(Image.open('images/garden.png'))
        self.fldImg = ImageTk.PhotoImage(Image.open('images/field.png'))
        self.stallImg = ImageTk.PhotoImage(Image.open('images/farm_stall.png'))
        self.wkshpImg = ImageTk.PhotoImage(Image.open('images/workshop.png'))
        self.grgImg = ImageTk.PhotoImage(Image.open('images/garage.png'))
        self.entImg = ImageTk.PhotoImage(Image.open('images/entrance.png'))
        self.barnImg = ImageTk.PhotoImage(Image.open('images/barn.png'))
        self.cknImg = ImageTk.PhotoImage(Image.open('images/chicken_coop.png'))

        # add a dictionary of buttons to use for available navigation options
        self.buttons = {
            'greenhouse': tk.Button(
                self.navFrame,
                image=self.ghsImg,
                command=lambda: self.location_changed("greenhouse")),
            'rose_garden': tk.Button(
                self.navFrame,
                image=self.rsegdnImg,
                command=lambda: self.location_changed("rose_garden")),
            'garden': tk.Button(
                self.navFrame,
                image=self.gdnImg,
                command=lambda: self.location_changed("garden")),
            'field': tk.Button(
                self.navFrame,
                image=self.fldImg,
                command=lambda: self.location_changed("field")),
            'farm_stall': tk.Button(
                self.navFrame, 
                image=self.stallImg,
                command=lambda: self.location_changed("farm_stall")),
            'workshop': tk.Button(
                self.navFrame,
                image=self.wkshpImg,
                command=lambda: self.location_changed("workshop")),
            'garage': tk.Button(
                self.navFrame,
                image=self.grgImg,
                command=lambda: self.location_changed("garage")),
            'entrance': tk.Button(
                self.navFrame,
                image=self.entImg,
                command=lambda: self.location_changed("entrance")),
            'barn': tk.Button(
                self.navFrame,
                image=self.barnImg,
                command=lambda: self.location_changed("barn")),
            'chicken_coop': tk.Button(
                self.navFrame,
                image=self.cknImg,
                command=lambda: self.location_changed("chicken_coop")),
        }
        self.buttons['greenhouse'].grid(row=0, column=0)
        self.buttons['rose_garden'].grid(row=0, column=1)
        self.buttons['garden'].grid(row=0, column=2)
        self.buttons['field'].grid(row=0, column=3)
        self.buttons['farm_stall'].grid(row=0, column=4)
        self.buttons['workshop'].grid(row=1, column=0)
        self.buttons['garage'].grid(row=1, column=1)
        self.buttons['entrance'].grid(row=1, column=2)
        self.buttons['barn'].grid(row=1, column=3)
        self.buttons['chicken_coop'].grid(row=1, column=4)

        #  Dictionary of the items to ensure only one instance of the item, copied everywhere.
        self.items = {
            "seeds": items.Seeds(),
            "water": items.Water(),
            "feed": items.Feed(),
            "manure": items.Manure(),
            "wheelbarrow": items.Wheelbarrow(),
            "eggs": items.Eggs(),
            "vegetables": items.Vegetables(),
            "herbs": items.Herbs(),
            "roses": items.Roses(),
            "honey": items.Honey(),
        }

        # dictionary of images to fetch correct images in a loop for each location.
        self.collect_images = {
            "seeds": ImageTk.PhotoImage(
                Image.open('images/seedpu.png')),
            "water": ImageTk.PhotoImage(
                Image.open('images/waterpu.png')),
            "feed": ImageTk.PhotoImage(
                Image.open('images/feedpu.png')),
            "manure": ImageTk.PhotoImage(
                Image.open('images/manurepu.png')),
            "wheelbarrow": ImageTk.PhotoImage(
                Image.open('images/wheelbarrowpu.png')),
            "eggs": ImageTk.PhotoImage(
                Image.open('images/eggpu.png')),
            "vegetables": ImageTk.PhotoImage(
                Image.open('images/vegpu.png')),
            "herbs": ImageTk.PhotoImage(
                Image.open('images/herbpu.png')),
            "roses": ImageTk.PhotoImage(
                Image.open('images/rosepu.png')),
            "honey": ImageTk.PhotoImage(
                Image.open('images/honeypu.png')),
        }

        self.drop_images = {
            "seeds": ImageTk.PhotoImage(
                Image.open('images/seedneg.png')),
            "water": ImageTk.PhotoImage(
                Image.open('images/waterneg.png')),
            "feed": ImageTk.PhotoImage(
                Image.open('images/feedneg.png')),
            "manure": ImageTk.PhotoImage(
                Image.open('images/manureneg.png')),
            "wheelbarrow": ImageTk.PhotoImage(
                Image.open('images/barrowneg.png')),
            "eggs": ImageTk.PhotoImage(
                Image.open('images/eggdrop.png')),
            "vegetables": ImageTk.PhotoImage(
                Image.open('images/vegneg.png')),
            "herbs": ImageTk.PhotoImage(
                Image.open('images/herbneg.png')),
            "roses": ImageTk.PhotoImage(
                Image.open('images/roseneg.png')),
            "honey": ImageTk.PhotoImage(
                Image.open('images/honeyneg.png')),
        }

        self.display_current_location()
        self.disable_buttons()

    def display_current_location(self):
        for widget in self.gameFrame.winfo_children():
            widget.destroy()  #  clear the Gameframe for the new current location
        self.locImg = ImageTk.PhotoImage(
            Image.open(f'images/{self.game.currently.name}.jpg'))
        self.bckgdImg = tk.Label(self.gameFrame, image=self.locImg)
        self.bckgdImg.place(x=0, y=0, relwidth=1, relheight=1)
        self.box = tk.Listbox(
            self.gameFrame, listvariable=self.inventoryVar, height=5, bg='light blue')  # fix the height of the inventory box

        loc = tk.Label(self.gameFrame, text=self.set_currentLocation_name(
            self.game.currently.name), bg='light blue')
        loc.pack(side=tk.BOTTOM)  # fix the current room title at the bottom
        self.pickups = self.create_pickup_collection()
        self.drops = self.create_drop_collection()
        self.set_button_states()
        self.display_players_current_inventory()

    def set_currentLocation_name(self, name):
        components = name.split('_')
        return ' '.join(x.title() for x in components)
    
    def create_pickup_collection(self):
        pickup_buttons = []
        pickup = self.game.getAvaialblePickUpItems()
        for i, item_name in enumerate(pickup):
            button = tk.Button(
                self.gameFrame,
                image=self.collect_images[item_name],
                command=partial(
                    self.add_to_inventory, self.items[item_name]))
            button.grid(row=i, column=0, sticky='E')
            pickup_buttons.append(
                (self.items[item_name], button)
            )
        return pickup_buttons

    def create_drop_collection(self):
        drop_buttons = []
        drop = self.game.getAvaialbleLeaveItems()
        for i, item_name in enumerate(drop):
            button = tk.Button(
                self.gameFrame,
                image=self.drop_images[item_name],
                command=partial(
                    self.remove_from_inventory, self.items[item_name]))
            button.grid(row=i, column=2, sticky='W')
            drop_buttons.append(
                (self.items[item_name], button)
            )
        return drop_buttons
    
    def set_button_states(self):
        for item, button in self.pickups:
            self.set_pu_button_state(button, item)

        for item, button in self.drops:
            self.set_dr_button_state(button, item)

    def set_pu_button_state(self, button, item):
        # get the matching case of the name of items in inventory so they can be compared
        if item.name.title() == 'Wheelbarrow':  # only/always colect 1 wheelbarrow
            if item.name.title() in self.game.getInventory():
                state = 'disabled'
            else:
                state = "normal"
        # only enable if you have capacity to pick up
        elif item.size <= self.game.player.capacity:
            state = "normal"
        else:
            state = "disabled"
        button['state'] = state
    
    def set_dr_button_state(self, button, item):
        if item.name.title() in self.game.getInventory(): # get the matching case of the name of items in inventory so they can be compared
            state = "normal"
        else:
            state = "disabled"  # filter so that buttons only show active if you have the item
        button['state'] = state

    def add_to_inventory(self, item):
        # update the inventory and reset button states on add.
        self.game.addItemtoInventory(item)
        self.inventoryVar.set(self.game.getInventory())
        self.set_button_states()

    def remove_from_inventory(self, item):
        # update the inventory and reset button states on remove.
        self.game.leaveItemAtLocation(item)
        self.inventoryVar.set(self.game.getInventory())
        self.set_button_states()

    def display_players_current_inventory(self):
        # showing the inventory as it changes
        self.box.grid(row=0, column=1)

    def disable_buttons(self):  # don't allow player to click on invalid moves
        exits = self.game.currently.exits
        for location_name, button in self.buttons.items():
            if location_name == self.game.currently.name:  # highlight 'you are here'
                button["state"] = "normal"
                button['relief'] = 'sunken'
                button['bg'] = 'red'  # background
                button['activebackground'] = 'red'
                button['bd'] = '5'
            elif location_name not in exits:  # invalid moves
                button["state"] = "disabled"
                button['relief'] = 'flat'
                button['bg'] = 'grey'
                button['bd'] = '5'  # pixels for the border
                button['foreground'] = 'white'
            else:  # possible moves
                button["state"] = "normal"
                button['bg'] = 'blue'
                button['bd'] = '5'
                button['activebackground'] = 'red' # adding mouseover

    def location_changed(self, loc_name):
        self.game.changeLocation(loc_name)
        self.display_current_location()
        self.disable_buttons()

    #  Functions below for populating the menubar
    def showAbout(self):
        messagebox.showinfo(
            'About', 'Click on an available location on the map to move, '
            'see what you can find to do the chores and get your pay from selling items at the farm stall. \n \n'
            'The black icons (left) are avialble to be picked up and can '
            "be taken to any location with it's negative active button (right). \n\n"
            'You have a limited capacity so if an item is not available try drop something first. '
            "You will see your items in your inventory when they're added."
            '\n\nCheck your account and hints in the menubar to help you. \n\nHave fun!')

    def showAccount(self):
        messagebox.showinfo(
            'Balance', f'You have £{self.game.getAccountBal()} Balance'
            )

    def showItems(self):
        messagebox.showinfo(
            'Collected Items', f'You have these items:{self.game.getInventory()}')

    def displayHint(self):
        hints = [
            'If you find the wheelbarrow you can carry more things',
            'Pick up items on your left and drop them on the right', 
            'Different locations have different items (to pick up and leave)',
            'The blue direction arrows on the map show possibly routes between locations',
            'Take your items to the Farm Stall so you can get money for them',
            'If you want to carry manure you will need the wheelbarrow',
            'You are limited by a set capacity, items have different capacities',
            'Did you check for eggs in the chicken coop?',
            'Roses are worth more than vegetables',
            'You can scroll down your inventory list to see what you have'
        ]
        messagebox.showinfo('Hint', random.choice(hints))


def main():
    # create window with title, size etc.
    win = tk.Tk()
    win.title('Farm Adventure World')
    win.geometry('1050x1080')
    win.resizable(True, True)

    # Create the GUI as a Frame
    # and attach it to the window ...
    myApp = App(win)

# Call the GUI mainloop ...
    log.info(' Starting game')
    win.mainloop()
    log.info(' Quit game')


if __name__ == '__main__':
    main()
