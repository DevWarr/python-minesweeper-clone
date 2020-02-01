from tkinter import *
from classes.GameFrame import GameFrame
from classes.ControlPanel import ControlPanel
from assets.all_assets import window_icon

root = Tk()
root.title("Minesweeper Clone")
root.iconbitmap(window_icon)

if __name__ == "__main__":

    GameFrame(root)
    root.mainloop()