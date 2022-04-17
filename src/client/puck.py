import pygame

import client.config as c
from client.game_object import GameObject


class Puck(pygame.sprite.Sprite, GameObject):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (c.WINDOW_WIDTH / 2, c.WINDOW_HEIGHT / 2)
