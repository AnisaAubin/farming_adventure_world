import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from game import Game
import random
from functools import partial

import items


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

        # Now we add images. These are stored in the images/ folder
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
        
        # Now add some useful widgets ...
        # self.textArea1 = tk.Label(self.gameFrame, text='whats here')
        # self.textArea1.pack()
        # self.cmdArea = tk.Entry(self.navFrame, text='testingCMD')
        # self.cmdArea.pack()
        # self.buildGUI()

    def display_current_location(self):
        for widget in self.gameFrame.winfo_children():
            widget.destroy()
        self.locImg = ImageTk.PhotoImage(
            Image.open(f'images/{self.game.currently.name}.jpg'))
        self.bckgdImg = tk.Label(self.gameFrame, image=self.locImg)
        self.bckgdImg.place(x=0, y=0, relwidth=1, relheight=1)
        self.box = tk.Listbox(
            self.gameFrame, listvariable=self.inventoryVar)

        loc = tk.Label(self.gameFrame, text=self.game.currently.name)
        loc.pack()
        self.display_contents()
        self.display_players_current_inventory()
        self.display_droppables()

    def display_contents(self):
        pickup = self.game.getAvaialblePickUpItems()
        for i, p in enumerate(pickup):
            item = tk.Button(
                self.gameFrame,
                image=self.collect_images[p],
                command=partial(self.add_to_inventory, self.items[p]))
            item.grid(row=i, column=0)

    def display_droppables(self):
        drop = self.game.getAvaialbleLeaveItems()
        for i, d in enumerate(drop):
            item = tk.Button(
                self.gameFrame,
                image=self.drop_images[d],
                command=partial(self.remove_from_inventory, self.items[d]))
            item.grid(row=i, column=2)

    def add_to_inventory(self, item):
        self.game.addItemtoInventory(item)
        self.inventoryVar.set(self.game.getInventory())

    def remove_from_inventory(self, item):
        self.game.leaveItemAtLocation(item)
        self.inventoryVar.set(self.game.getInventory())

    def display_players_current_inventory(self):
        self.box.grid(row=0, column=1)

    def disable_buttons(self):
        exits = self.game.currently.exits
        for location_name, button in self.buttons.items():
            if location_name == self.game.currently.name:
                button["state"] = "normal"
                button['relief'] = 'sunken'
                button['bg'] = 'red'
                button['activebackground'] = 'red'
                button['bd'] = '5'
            elif location_name not in exits:
                button["state"] = "disabled"
                button['relief'] = 'flat'
                button['bg'] = 'grey'
                button['bd'] = '5'
                button['foreground'] = 'white'
            else:
                button["state"] = "normal"
                button['bg'] = 'blue'
                button['bd'] = '5'
                button['activebackground'] = 'red'

    def location_changed(self, loc_name):
        self.game.changeLocation(loc_name)
        self.display_current_location()
        self.disable_buttons()

    def showAbout(self):
        messagebox.showinfo(
            'About', 'Click on an available location on the map to move,'
            'see what you can find to do the chores and get your pay')

    def showAccount(self):
        messagebox.showinfo(
            'Balance', f'You have £{self.game.getAccountBal()} Balance')

    def showItems(self):
        messagebox.showinfo(
            'Collected Items', f'You have these items:{self.game.getInventory()} ')

    def displayHint(self):
        hints = [
            'If you find the wheelbarrow you can carry more things',
            'Take your items to the stall so you can get money for them',
            'If you want to carry manure you will need the wheelbarrow',
            'Did you check for eggs in the chicken coop',
            'Roses are worth more than vegetables'
        ]
        messagebox.showinfo('Hint', random.choice(hints))


def main():
    # create window with title, size etc.
    win = tk.Tk()
    win.title('Farm Adventure World')
    win.geometry('800x600')
    win.resizable(False, False)

    # Create the GUI as a Frame
    # and attach it to the window ...
    myApp = App(win)

# Call the GUI mainloop ...
    win.mainloop()


def Showavailableitems(location):
    return location.collectableitems


if __name__ == '__main__':
    main()
