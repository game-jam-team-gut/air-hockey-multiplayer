import pygame

import client.config as c
from client.game_object import GameObject


class Striker(pygame.sprite.Sprite, GameObject):
    def __init__(self, img, y, board_rect):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (c.WINDOW_WIDTH / 2, y)
        self.is_dragged = False
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 0.0
        self.board_rect = board_rect

    def update_pos(self, player_input):
        if player_input.dragging:
            m_pos = pygame.mouse.get_pos()
            m_rect = pygame.Rect(m_pos[0] - self.rect.w / 2, m_pos[1] - self.rect.h / 2, self.rect.w, self.rect.h)
            if (self.is_dragged or self.rect.collidepoint(m_pos)) and self.board_rect.contains(m_rect):
                self.set_position(m_pos)
            if self.rect.collidepoint(m_pos):
                self.is_dragged = True
        else:
            self.is_dragged = False
