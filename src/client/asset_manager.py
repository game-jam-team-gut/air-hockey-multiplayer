import pygame
from os import path

import client.config as c
import shared.config as sc

DIGITS_NUMBER = 10


class AssetManager:
    def __init__(self):
        self.board_img = pygame.image.load(path.join(c.ASSETS_FOLDER, 'board.png'))
        self.play_area_img = pygame.image.load(path.join(c.ASSETS_FOLDER, 'play_area.png'))
        self.striker_img = pygame.image.load(path.join(c.ASSETS_FOLDER, 'striker.png'))
        self.puck_img = pygame.image.load(path.join(c.ASSETS_FOLDER, 'puck.png'))

    @staticmethod
    def scale_img(img):
        return pygame.transform.smoothscale(img, (img.get_width() * sc.SCALE, img.get_height() * sc.SCALE))
