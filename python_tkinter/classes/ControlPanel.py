from tkinter import *
from classes.GameFrame import GameFrame
from classes.GameTile import GameTile
from assets.all_assets import other_tiles
from PIL import ImageTk

class ControlPanel:

    def __init__(self, master):
        self.main_game = Frame(master, width=200, height=200)
        self.main_game.pack()
        self.play_button   = Button(self.main_game, text="Play")
        self.play_button.grid()
        self.label         = GameTile(self,0,0)
        self.label2        = Label(self.main_game, width=32, height=32)
        self.label2.grid()
        temp_img = ImageTk.PhotoImage(other_tiles["Unrevealed"])
        self.label2.configure(image=temp_img)
        self.label.image = temp_img