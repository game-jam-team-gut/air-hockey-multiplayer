import pygame

import shared.config as sc
from client.game_object import GameObject


class Board(pygame.sprite.Sprite, GameObject):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect(center=(sc.WINDOW_WIDTH / 2, sc.WINDOW_HEIGHT / 2))
