from tkinter import *
import classes.tile_states as tile_states
from random import randint
from classes.GameTile import GameTile

class GameFrame:

    def __init__(self, master, array_size = 15, number_of_mines = 20):
        self.main_game        = Frame(master, width=500, height=500)
        self.total_mines      = number_of_mines
        self.unrevealed_tiles = array_size*array_size
        self.flagged_mines    = 0
        self.tile_list        = []
        self.array_size       = array_size
        self.state            = "wait" # Possible states: "wait", "play", "lose", "win"

        # Attach to window
        self.main_game.pack()
        self.start()

    def start(self):
        self.state = "play"
        # Create Empty 2d array and place mines
        self.create_empty_board()
        self.place_mines()

        # Turn 2d array of integers into a 2d array of Game Tiles
        self.attach_tiles()

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

    def update_unrevealed_tiles(self, tile_count):
        self.unrevealed_tiles -= tile_count
        print(f"{self.unrevealed_tiles}: {self.total_mines}")
        if (self.unrevealed_tiles == self.total_mines and 
                    self.state   == "play"):
            self.win_game()

    def change_tile_state(self, tile, new_state):
        tile.state = new_state
        tile.state.on_enter()
        if isinstance(new_state, tile_states.RevealedState):
            self.update_unrevealed_tiles(1)

    def change_many_tile_states(self, tile_list, new_state):
        for tile in tile_list:
            tile.state = new_state(self, tile)
        [tile.state.on_enter() for tile in tile_list]
        if type(new_state) == type(tile_states.RevealedState):
            self.update_unrevealed_tiles(len(tile_list))
    
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
            self.change_many_tile_states(newly_revealed_tiles, tile_states.RevealedState)
        
        # Set our selected tile's value to the number of surrounding mines we have
        selected_tile.value = surrounding_mines

    # If there's a tile at this location, return the tile
    # Otherwise, return None
    def tile_at(self, row, column):
        if (row    >= 0 and row    < self.array_size and 
            column >= 0 and column < self.array_size):
            return self.tile_list[row][column]
        else:
            return None

    def win_game(self):
        self.state = "win"
        print("WIN")

    def lose_game(self):
        # If we've already lost, exit the function
        if self.state == "lose":
            return
        self.state = "lose"
        print("LOSE")
        # Reveal all bomb tiles that haven't been flagged
        [   [   self.change_tile_state(tile, tile_states.RevealedState(self, tile)) 
                for tile 
                in tile_array 
                if isinstance(tile.state, tile_states.UnrevealedState) 
                    and tile.value == 9]
            for tile_array
            in self.tile_list]