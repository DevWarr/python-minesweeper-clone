from abc import ABC


# ================== ABSTRACT CLASS ==================== #

class TileState(ABC):

    def __init__(self, master, tile):
        self.master = master
        self.tile = tile

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
        return super().on_enter()

    def on_mousedown(self, event):
        return super().on_mousedown(event)
    
    def on_mouseup(self, event):
        return super().on_mouseup(event)
    
    def on_rightclick(self, event):
        return super().on_rightclick(event)



# ================== FLAGGED STATE ==================== #

class FlaggedState(TileState):

    def __init__(self, master, tile):
        super().__init__(master, tile)

    def on_enter(self):
        return super().on_enter()

    def on_mousedown(self, event):
        return super().on_mousedown(event)
    
    def on_mouseup(self, event):
        return super().on_mouseup(event)
    
    def on_rightclick(self, event):
        return super().on_rightclick(event)



# =================== REVEALED STATE ===================== #

class RevealedState(TileState):

    def __init__(self, master, tile):
        super().__init__(master, tile)

    def on_enter(self):
        return super().on_enter()

    def on_mousedown(self, event):
        return super().on_mousedown(event)
    
    def on_mouseup(self, event):
        return super().on_mouseup(event)
    
    def on_rightclick(self, event):
        return super().on_rightclick(event)