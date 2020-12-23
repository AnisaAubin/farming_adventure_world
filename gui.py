import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from game import Game
import random


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
        self.gameFrame = tk.Frame(
            root, width=800, height=300, bg='WHITE', borderwidth=3)
        self.gameFrame.pack_propagate(0)   # Prevents resizing
        self.navFrame = tk.Frame(
            root, width=800, height=300, bg='GREY', borderwidth=3)
        self.navFrame.grid_propagate(0)   # Prevents resizing
        # This packs both frames into the root window ...
        self.gameFrame.pack()
        self.navFrame.pack()

        # add buttons to the menubar 
        menubar = tk.Menu()
        menubar.add_command(label='About', command=self.showAbout)
        menubar.add_command(label='Account', command=self.showAccount)
        menubar.add_command(label='Hints', command=self.displayHint)
        menubar.add_command(label='Quit', command=root.destroy)
        root.config(menu=menubar)

        # Now we add images. These are stored in the images/ folder
        self.ghsImg = ImageTk.PhotoImage(Image.open('images/greenhouse.png')) 
        self.rsegdnImg = ImageTk.PhotoImage(Image.open('images/greenhouse.png'))
        self.gdnImg = ImageTk.PhotoImage(Image.open('images/greenhouse.png'))
        self.fldImg = ImageTk.PhotoImage(Image.open('images/greenhouse.png'))
        self.stallImg = ImageTk.PhotoImage(Image.open('images/greenhouse.png'))
        self.wkshpImg = ImageTk.PhotoImage(Image.open('images/greenhouse.png'))
        self.grgImg = ImageTk.PhotoImage(Image.open('images/greenhouse.png'))
        self.entImg = ImageTk.PhotoImage(Image.open('images/greenhouse.png'))
        self.barnImg = ImageTk.PhotoImage(Image.open('images/greenhouse.png'))
        self.cknImg = ImageTk.PhotoImage(Image.open('images/greenhouse.png'))

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
        loc = tk.Label(self.gameFrame, text=self.game.currently.name)
        loc.pack()

    def disable_buttons(self):
        exits = self.game.currently.exits
        for location_name, button in self.buttons.items():
            if location_name not in exits:
                button["state"] = "disabled"
            else:
                button["state"] = "normal"

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
