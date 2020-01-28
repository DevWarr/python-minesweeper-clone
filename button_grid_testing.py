from tkinter import *

root = Tk()
root.title("Minesweeper Clone")

tile_unrevealed = PhotoImage(file="./assets/TileUnrevealed.png")
tile_selected   = PhotoImage(file="./assets/TileSelected.png")
tile_revealed   = PhotoImage(file="./assets/TileRevealed.png")

class game_tile:

    def __init__(self, master_class, row_number, column_number):
        self.main_class = master_class
        self.row_number = row_number
        self.column_number = column_number
        self.selected = False
        self.revealed = False

        self.tile = Label(self.main_class.main_game, image=tile_unrevealed, width=32, height=32)
        self.tile.grid(row=self.row_number, column=self.column_number)

        self.tile.bind("<Button-1>", lambda event: self.main_class.select_label(self))
        self.tile.bind("<ButtonRelease-1>", lambda event: self.main_class.unselect_label(event, self))

    def set_image(self, new_image):
        self.tile.configure(image=new_image)
        self.tile.image = new_image

    def update(self):
        print(f"\n{self}\nSelected: {self.selected}\nRevealed: {self.revealed}")
        # If it's revealed, it stays revealed. No matter what.
        if self.revealed:
            self.set_image(tile_revealed)
        # Otherwise, change the image to either selected or unrevealed
        else:
            if self.selected:
                self.set_image(tile_selected)
            else:
                self.set_image(tile_unrevealed)

    def __str__(self):
        return f"{self.tile}"


class game_frame:

    def __init__(self, master):
        self.main_game = Frame(master, width=500, height=500)
        self.tile_list = []
        self.selected_tile = None

        for row_number in range(10):
            self.tile_list.append([])
            for column_number in range(10):
                tile = game_tile(self, row_number, column_number)
                self.tile_list[row_number].append(tile)

        self.main_game.grid()

    def select_label(self, game_tile):
        self.selected_tile = game_tile
        self.selected_tile.selected = True
        game_tile.update()

    def unselect_label(self, event, game_tile):
        # Making sure that we are lifting the mouse button on the actual label
        if (event.x > 0 and event.x < game_tile.tile.winfo_width() and
            event.y > 0 and event.y < game_tile.tile.winfo_height()):
            self.selected_tile.revealed = True

        self.selected_tile.selected = False
        self.selected_tile.update()
        self.selected_tile = None


if __name__ == "__main__":

    game_frame(root)
    root.mainloop()