from abc import ABC, abstractmethod
from assets.all_assets import number_tiles, other_tiles

# ================== ABSTRACT CLASS ==================== #

class TileState(ABC):

    def __init__(self, master, tile):
        self.master = master
        self.tile_class = tile

    def is_clicked(self, event):
        return (event.x > 0 and event.x < self.tile_class.tile.winfo_width() and
                event.y > 0 and event.y < self.tile_class.tile.winfo_height())

    @abstractmethod
    def on_enter(self):
        pass
    
    @abstractmethod
    def on_mousedown(self, event):
        pass

    @abstractmethod
    def on_mouseup(self, event):
        pass

    @abstractmethod
    def on_rightclick(self, event):
        pass



# ================== UNREVEALED STATE ==================== #

class UnrevealedState(TileState):

    def __init__(self, master, tile):
        super().__init__(master, tile)

    def on_enter(self):
        self.tile_class.set_image(other_tiles["Unrevealed"])

    def on_mousedown(self, event):
        self.tile_class.set_image(other_tiles["Selected"])
    
    def on_mouseup(self, event):
        if (self.is_clicked(event)):
            self.tile_class.change_state(RevealedState(self.master, self.tile_class))
        else:
            self.tile_class.set_image(other_tiles["Unrevealed"])
    
    def on_rightclick(self, event):
        self.tile_class.change_state(FlaggedState(self.master, self.tile_class))



# ================== FLAGGED STATE ==================== #

class FlaggedState(TileState):

    def __init__(self, master, tile):
        super().__init__(master, tile)

    def on_enter(self):
        self.tile_class.set_image(other_tiles["Flagged"])

    def on_mousedown(self, event):
        return super().on_mousedown(event)
    
    def on_mouseup(self, event):
        return super().on_mouseup(event)
    
    def on_rightclick(self, event):
        self.tile_class.change_state(UnrevealedState(self.master, self.tile_class))



# =================== REVEALED STATE ===================== #

class RevealedState(TileState):

    def __init__(self, master, tile):
        super().__init__(master, tile)

    def on_enter(self):
        if self.tile_class.value == 9:
            self.tile_class.set_image(number_tiles[9])
            self.master.lose_game()
        else:
            # self.master.check_for_mines(self.tile.row_number, self.tile.column_number)
            self.tile_class.set_image(number_tiles[0])

    def on_mousedown(self, event):
        return super().on_mousedown(event)
    
    def on_mouseup(self, event):
        return super().on_mouseup(event)
    
    def on_rightclick(self, event):
        return super().on_rightclick(event)