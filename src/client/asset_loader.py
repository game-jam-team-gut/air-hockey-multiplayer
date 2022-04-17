import pygame
from os import path


class AssetLoader:
    def __init__(self):
        self.board_img = pygame.image.load(path.join('assets', 'board.png'))
        self.striker_img = pygame.image.load(path.join('assets', 'striker.png'))
        self.puck_img = pygame.image.load(path.join('assets', 'puck.png'))
        self.result_bg_big_img = pygame.image.load(path.join('assets', 'result_bg_big.png'))
        self.result_bg_small_img = pygame.image.load(path.join('assets', 'result_bg_small.png'))
        self.colon_img = pygame.image.load(path.join('assets', 'colon.png'))

        for i in range(10):
            self.numbers_img.append(pygame.image.load(path.join('assets', str(i) + '.png')))

    board_img = None
    striker_img = None
    puck_img = None
    result_bg_big_img = None
    result_bg_small_img = None
    colon_img = None
    numbers_img = []
