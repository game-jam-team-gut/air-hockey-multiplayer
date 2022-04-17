from asset_loader import AssetLoader
from board import Board
from striker import Striker
import pygame
import config

STRIKERS_NUMBER = 2


# no idea where to put these two functions
def scale_img(img, scale):
    return pygame.transform.smoothscale(img, (img.get_size()[0] * scale, img.get_size()[1] * scale))


def scale_imgs(imgs, scale):
    scaled_imgs = []
    for img in imgs:
        scaled_imgs.append(pygame.transform.smoothscale(img, (img.get_size()[0] * scale, img.get_size()[1] * scale)))
    return scaled_imgs


class Game:
    def __init__(self) -> None:
        self.asset_loader = AssetLoader()
        self.board = Board(scale_img(self.asset_loader.board_img, config.SCALE))
        self.strikers[0] = Striker(scale_img(self.asset_loader.striker_img, config.SCALE), config.WINDOW_WIDTH/2, 50)
        self.strikers[1] = Striker(scale_img(self.asset_loader.striker_img, config.SCALE), config.WINDOW_WIDTH/2, 800)

    def draw(self, window):
        window.fill((255, 255, 255))
        self.board.draw(window)
        for striker in self.strikers:
            striker.draw(window)

    def update(self):
        pass

    asset_loader = None
    board = None
    strikers = [None for _ in range(STRIKERS_NUMBER)]
