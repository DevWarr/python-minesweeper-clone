from PIL import Image
import os

FILEPATH = os.path.dirname(__file__)

number_tiles = {
    "Zero": Image.open(os.path.join(FILEPATH, "TileZero.png")),
    "One": Image.open(os.path.join(FILEPATH, "TileOne.png")),
    "Two": Image.open(os.path.join(FILEPATH, "TileTwo.png")),
    "Three": Image.open(os.path.join(FILEPATH, "TileThree.png")),
    "Four": Image.open(os.path.join(FILEPATH, "TileFour.png")),
    "Five": Image.open(os.path.join(FILEPATH, "TileFive.png")),
    "Six": Image.open(os.path.join(FILEPATH, "TileSix.png")),
    "Seven": Image.open(os.path.join(FILEPATH, "TileSeven.png")),
    "Eight": Image.open(os.path.join(FILEPATH, "TileEight.png")),
    "Bomb": None
}

other_tiles = {
    "Unrevealed": Image.open(os.path.join(FILEPATH, "TileUnrevealed.png")),
    "Selected": Image.open(os.path.join(FILEPATH, "TileSelected.png")),
    "Flagged": Image.open(os.path.join(FILEPATH, "TileFlagged.png"))
}


print("Done!")