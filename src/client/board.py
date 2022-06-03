import shared.config as sc
from client.game_object import GameObject


class Board(GameObject):
    def __init__(self, img):
        super().__init__(img, sc.WINDOW_WIDTH / 2, sc.WINDOW_HEIGHT / 2)
