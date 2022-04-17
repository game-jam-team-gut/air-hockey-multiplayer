import pygame
from os import path

import config


class AssetManager:
    def __init__(self):
        self.board_img = pygame.image.load(path.join('assets', 'board.png'))
        self.striker_img = pygame.image.load(path.join('assets', 'striker.png'))
        self.puck_img = pygame.image.load(path.join('assets', 'puck.png'))
        self.result_bg_big_img = pygame.image.load(path.join('assets', 'result_bg_big.png'))
        self.result_bg_small_img = pygame.image.load(path.join('assets', 'result_bg_small.png'))
        self.colon_img = pygame.image.load(path.join('assets', 'colon.png'))

        self.numbers_img = []
        for i in range(10):
            self.numbers_img.append(pygame.image.load(path.join('assets', str(i) + '.png')))

    @staticmethod
    def scale_img(img):
        return pygame.transform.smoothscale(img, (img.get_size()[0] * config.SCALE, img.get_size()[1] * config.SCALE))

    @staticmethod
    def scale_imgs(imgs):
        scaled_imgs = []
        for img in imgs:
            scaled_imgs.append(
                pygame.transform.smoothscale(img, (img.get_size()[0] * config.SCALE, img.get_size()[1] * config.SCALE)))
        return scaled_imgs
