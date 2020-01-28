from tkinter import *
from classes.GameFrame import GameFrame

root = Tk()
root.title("Minesweeper Clone")

if __name__ == "__main__":

    GameFrame(root)
    root.mainloop()