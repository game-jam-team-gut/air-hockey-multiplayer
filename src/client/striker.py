import pygame

import client.config as c
from client.game_object import GameObject


class Striker(pygame.sprite.Sprite, GameObject):
    def __init__(self, img, y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (c.WINDOW_WIDTH / 2, y)
        self.is_dragged = False
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 0.0

    def update_pos(self, player_input):
        mouse_pos = pygame.mouse.get_pos()
        if player_input.dragging:
            if self.is_dragged:
                self.set_position(mouse_pos)
            elif self.rect.collidepoint(mouse_pos):
                self.set_position(mouse_pos)
                self.is_dragged = True
        else:
            self.is_dragged = False
