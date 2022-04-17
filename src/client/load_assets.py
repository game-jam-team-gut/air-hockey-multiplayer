import pygame
from os import path

numbers_img = []
for number in range(10):
    numbers_img.append(pygame.image.load(path.join('assets', str(number) + '.png')))

colon_img = pygame.image.load(path.join('assets', 'colon.png'))
board_img = pygame.image.load(path.join('assets', 'board.png'))
striker_img = pygame.image.load(path.join('assets', 'striker.png'))
puck_img = pygame.image.load(path.join('assets', 'puck.png'))
result_bg_big_img = pygame.image.load(path.join('assets', 'result_bg_big.png'))
result_bg_small_img = pygame.image.load(path.join('assets', 'result_bg_small.png'))
