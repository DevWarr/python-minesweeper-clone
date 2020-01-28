from tkinter import *
import classes.tile_states as tile_states
from random import randint
from classes.GameTile import GameTile

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

    def change_many_tile_states(self, tile_list):
        for tile in tile_list:
            print(tile)
            tile.state = tile_states.RevealedState(self, tile)
        [tile.state.on_enter() for tile in tile_list]

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
    
    # Check all eight surrounding tiles to see how many mines there are.
    # If there are no mines surrounding this tile,
    #     reveal all the unrevealed surrounding tiles automatically.
    def check_for_mines(self, row, column):
        selected_tile = self.tile_list[row][column]
        surrounding_tiles = [ # Creating list of tiles
            self.tile_at(row - 1, column - 1),
            self.tile_at(row - 1, column    ),
            self.tile_at(row - 1, column + 1),
            self.tile_at(row    , column + 1),
            self.tile_at(row + 1, column + 1),
            self.tile_at(row + 1, column    ),
            self.tile_at(row + 1, column - 1),
            self.tile_at(row    , column - 1),
        ]

        # Looping through our list and adding one if there is a mine
        surrounding_mines = 0
        for tile in surrounding_tiles:
            if tile != None and tile.value == 9:
                surrounding_mines += 1

        # If there are 0 surrounding mines, reveal all of the surrounding mines at once
        if surrounding_mines == 0:
            newly_revealed_tiles = [tile for tile 
                                    in surrounding_tiles 
                                    if tile != None and 
                                    not isinstance(tile.state, tile_states.RevealedState) ]
            self.change_many_tile_states(newly_revealed_tiles)
        
        # Set our selected tile's value to the number of surrounding mines we have
        selected_tile.value = surrounding_mines

    # If there's a tile at this location, return the tile
    # Otherwise, return None
    def tile_at(self, row, column):
        if (row >= 0 and row < self.array_size and 
            column >= 0 and column < self.array_size):
            return self.tile_list[row][column]
        else:
            return None

    def lose_game(self):
        pass