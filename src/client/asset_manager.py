import pygame
from os import path

import client.config as c

DIGITS_NUMBER = 10


class AssetManager:
    def __init__(self):
        self.board_img = pygame.image.load(path.join(c.ASSETS_FOLDER, 'board.png'))
        self.striker_img = pygame.image.load(path.join(c.ASSETS_FOLDER, 'striker.png'))
        self.puck_img = pygame.image.load(path.join(c.ASSETS_FOLDER, 'puck.png'))
        self.result_bg_big_img = pygame.image.load(path.join(c.ASSETS_FOLDER, 'result_bg_big.png'))
        self.result_bg_small_img = pygame.image.load(path.join(c.ASSETS_FOLDER, 'result_bg_small.png'))
        self.colon_img = pygame.image.load(path.join(c.ASSETS_FOLDER, 'colon.png'))

        self.digits_img = []
        for digit in range(DIGITS_NUMBER):
            self.digits_img.append(pygame.image.load(path.join(c.ASSETS_FOLDER, str(digit) + '.png')))

    @staticmethod
    def scale_img(img):
        return pygame.transform.smoothscale(img, (img.get_width() * c.SCALE, img.get_height() * c.SCALE))

    @staticmethod
    def scale_imgs(imgs):
        scaled_imgs = []
        for img in imgs:
            scaled_imgs.append(
                pygame.transform.smoothscale(img, (img.get_width() * c.SCALE, img.get_height() * c.SCALE)))
        return scaled_imgs
