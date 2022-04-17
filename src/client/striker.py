import pygame

import client.config as c
from client.game_object import GameObject

class Striker(pygame.sprite.Sprite, GameObject):
    def __init__(self, img, y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (c.WINDOW_WIDTH / 2 - self.image.get_width() / 2, y)
