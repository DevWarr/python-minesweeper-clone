from PIL import Image
import os

FILEPATH = os.path.dirname(__file__)

number_tiles = [
    Image.open(os.path.join(FILEPATH, "TileZero.png")),  # 0
    Image.open(os.path.join(FILEPATH, "TileOne.png")),   # 1
    Image.open(os.path.join(FILEPATH, "TileTwo.png")),   # 2
    Image.open(os.path.join(FILEPATH, "TileThree.png")), # 3
    Image.open(os.path.join(FILEPATH, "TileFour.png")),  # 4
    Image.open(os.path.join(FILEPATH, "TileFive.png")),  # 5
    Image.open(os.path.join(FILEPATH, "TileSix.png")),   # 6
    Image.open(os.path.join(FILEPATH, "TileSeven.png")), # 7
    Image.open(os.path.join(FILEPATH, "TileEight.png")), # 8
    Image.open(os.path.join(FILEPATH, "TileBomb.png")),  # 9
]

other_tiles = {
    "Unrevealed": Image.open(os.path.join(FILEPATH, "TileUnrevealed.png")),
    "Selected": Image.open(os.path.join(FILEPATH, "TileSelected.png")),
    "Flagged": Image.open(os.path.join(FILEPATH, "TileFlagged.png"))
}

# Here, we don't want to open the image, but rather to keep a file path to the image
window_icon = os.path.join(FILEPATH, "BombIcon.ico")