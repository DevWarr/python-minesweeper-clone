from tkinter import *
from random import randint
import tile_states
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

        self.tile.bind("<Button-1>", lambda event: self.state.on_mousedown(event))
        self.tile.bind("<ButtonRelease-1>", lambda event: self.state.on_mouseup(event))
        self.tile.bind("<Button-3>", lambda event: self.state.on_rightclick(event))

    def set_image(self, new_image):
        tile_image = ImageTk.PhotoImage(new_image)
        self.tile.configure(image=tile_image)
        self.tile.image = tile_image
    
    def change_state(self, new_state):
        self.state = new_state
        self.state.on_enter()

    def __str__(self):
        return f"{self.tile}"


class GameFrame:

    def __init__(self, master, array_size = 15, number_of_mines = 20):
        self.main_game     = Frame(master, width=500, height=500)
        self.total_mines   = number_of_mines
        self.flagged_mines = 0
        self.tile_list     = []
        self.array_size    = array_size

        # Create Empty 2d array and place mines
        self.create_empty_board()
        self.place_mines()

        # Turn 2d array of integers into a 2d array of Game Tiles
        self.attach_tiles()

        # Attach to window
        self.main_game.grid()

    def create_empty_board(self):
        for row_number in range(self.array_size):
            self.tile_list.append([0 for i in range(self.array_size)])

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.total_mines:
            row    = randint(0, self.array_size - 1)
            column = randint(0, self.array_size - 1)
            if (self.tile_list[row][column] != 9):
                self.tile_list[row][column] = 9
                mines_placed += 1
            else:
                continue

    def attach_tiles(self):

        temp_tileset = []

        def create_GameTile(row, column, num):
            if num == 9:
                return GameTile(self, row, column, num)
            else:
                return GameTile(self, row, column)
                
        for row , num_array in enumerate(self.tile_list):
            temp_tileset.append(
                [create_GameTile(row, column, num) for column, num in enumerate(num_array)]
            )
        self.tile_list = temp_tileset
    
    def check_for_mines(self, row, column):
        selected_tile = self.tile_list[row][column]
        # surrounding_tiles = [
        #     self.tile_list[row - 1][column - 1],
        #     self.tile_list[row - 1][column    ],
        #     self.tile_list[row - 1][column + 1],
        #     self.tile_list[row    ][column + 1],
        #     self.tile_list[row + 1][column + 1],
        #     self.tile_list[row + 1][column    ],
        #     self.tile_list[row + 1][column - 1],
        #     self.tile_list[row    ][column - 1],
        # ]

    def lose_game(self):
        pass