from tkinter import *
import classes.tile_states as tile_states
from PIL import ImageTk

class GameTile:

    def __init__(self, master_class, row_number, column_number, value = None):
        self.main_class = master_class
        self.row_number = row_number
        self.column_number = column_number
        self.value = value

        self.tile = Label(self.main_class.main_game, width=32, height=32)
        self.tile.grid(row=self.row_number, column=self.column_number)
        
        self.state = tile_states.UnrevealedState(master_class, self)
        self.state.on_enter()

        self.tile.bind("<Button-1>",        lambda event: self.handle_event(event, self.state.on_mousedown))
        self.tile.bind("<ButtonRelease-1>", lambda event: self.handle_event(event, self.state.on_mouseup))
        self.tile.bind("<Button-3>",        lambda event: self.handle_event(event, self.state.on_rightclick))

    def set_image(self, new_image):
        tile_image = ImageTk.PhotoImage(new_image)
        self.tile.configure(image=tile_image)
        self.tile.image = tile_image

    # Make sure that we only handle clicks if we're in play mode
    def handle_event(self, event, callback):
        if self.main_class.state != "play":
            return 
        callback(event)

    def __str__(self):
        return f"{self.tile}"


