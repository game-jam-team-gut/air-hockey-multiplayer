import pygame
import pymunk
import math

import shared.config as sc
from client.physics_game_object import PhysicsGameObject

MASS = 100
ELASTICITY = 1


class Striker(PhysicsGameObject):
    def __init__(self, img, y):
        super().__init__(img, sc.STRIKER_START_X, y, MASS, ELASTICITY)
        self.velocity = 0.0
        self.is_dragged = False
        self.is_primary_sync = False
        self.body.body_type = pymunk.Body.KINEMATIC

    def position_change(self, old_pos):
        new_pos = self.get_position()
        return math.sqrt((old_pos[0] - new_pos[0]) ** 2 + (old_pos[1] - new_pos[1]) ** 2)

    def change_by_mouse_position(self, m_pos, p_movement_area):
        m_rect = pygame.Rect(m_pos[0] - self.rect.w / 2, m_pos[1] - self.rect.h / 2, self.rect.w, self.rect.h)
        if p_movement_area.contains(m_rect):
            self.set_position(m_pos)
        else:
            if m_rect.x + m_rect.width > p_movement_area.x + p_movement_area.width:
                self.set_position(
                    (p_movement_area.x + p_movement_area.width - m_rect.width / 2, self.get_position()[1]))
            elif m_rect.x < p_movement_area.x:
                self.set_position((p_movement_area.x + m_rect.width / 2, self.get_position()[1]))
            else:
                self.set_position((m_rect.x + m_rect.width / 2, self.get_position()[1]))
            if m_rect.y < p_movement_area.y:
                self.set_position((self.get_position()[0], p_movement_area.y + self.rect.height / 2))
            elif m_rect.y + m_rect.height > p_movement_area.y + p_movement_area.height:
                self.set_position((self.get_position()[0],
                                  p_movement_area.y + p_movement_area.height - m_rect.height / 2))
            else:
                self.set_position((self.get_position()[0], m_rect.y + m_rect.height / 2))

    def check_player_input(self, p_input, p_movement_area):
        old_pos = self.get_position()
        if p_input.dragging:
            m_pos = pygame.mouse.get_pos()
            if self.is_dragged or self.rect.collidepoint(m_pos):
                self.change_by_mouse_position(m_pos, p_movement_area)
            if self.rect.collidepoint(m_pos):
                self.is_dragged = True
        else:
            self.is_dragged = False
        self.velocity = self.position_change(old_pos)
