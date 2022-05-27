import pygame
import pymunk
import math

import shared.config as sc
from client.physics_game_object import PhysicsGameObject

MASS = 100
ELASTICITY = 1


class Striker(PhysicsGameObject):
    def __init__(self, img, y):
        super().__init__(img, sc.WINDOW_WIDTH / 2, y, MASS, ELASTICITY)
        self.velocity = 0.0
        self.is_dragged = False
        self.is_primary_sync = False
        self.body.body_type = pymunk.Body.KINEMATIC

    def position_change(self, old_pos):
        new_pos = self.get_position()
        return math.sqrt((old_pos[0] - new_pos[0]) ** 2 + (old_pos[1] - new_pos[1]) ** 2)

    def change_by_mouse_position(self, m_pos, board_rect):
        m_rect = pygame.Rect(m_pos[0] - self.rect.w / 2, m_pos[1] - self.rect.h / 2, self.rect.w, self.rect.h)
        if board_rect.contains(m_rect):
            self.set_position(m_pos)
        else:
            m_x_rect = pygame.Rect(m_pos[0] - self.rect.w / 2, self.rect.top, self.rect.w, self.rect.h)
            if board_rect.contains(m_x_rect):
                self.set_position((m_x_rect.centerx, m_x_rect.centery))
            m_y_rect = pygame.Rect(self.rect.left, m_pos[1] - self.rect.h / 2, self.rect.w, self.rect.h)
            if board_rect.contains(m_y_rect):
                self.set_position((m_y_rect.centerx, m_y_rect.centery))

    def check_player_input(self, player_input, board_rect):
        old_pos = self.get_position()
        if player_input.dragging:
            m_pos = pygame.mouse.get_pos()
            if self.is_dragged or self.rect.collidepoint(m_pos):
                self.change_by_mouse_position(m_pos, board_rect)
            if self.rect.collidepoint(m_pos):
                self.is_dragged = True
        else:
            self.is_dragged = False
        self.velocity = self.position_change(old_pos)
