import pygame
import math

import client.config as c
from client.game_object import GameObject


class Puck(pygame.sprite.Sprite, GameObject):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (c.WINDOW_WIDTH / 2, c.WINDOW_HEIGHT / 2)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 0.0
        self.col_angle_rads = 0.0

    def update_pos(self):
        new_x = self.rect.center[0] + (self.speed * math.cos(self.col_angle_rads))
        new_y = self.rect.center[1] + (self.speed * math.sin(self.col_angle_rads))
        self.rect.center = new_x, new_y

    def slow_down(self):
        if self.speed > 0:
            self.speed = self.speed - self.speed/25
        else:
            self.speed = 0.0
