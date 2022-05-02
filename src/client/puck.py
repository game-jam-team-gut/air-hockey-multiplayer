import pygame
import math

import shared.config as sc
from client.game_object import GameObject


class Puck(pygame.sprite.Sprite, GameObject):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (sc.WINDOW_WIDTH / 2, sc.WINDOW_HEIGHT / 2)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 0.0
        self.col_angle_rads = 0.0

    def reverse_angle(self):
        if self.col_angle_rads > 0:
            self.col_angle_rads = self.col_angle_rads + math.pi / 2
        else:
            self.col_angle_rads = self.col_angle_rads - math.pi / 2

    def update_speed(self):
        if self.speed > 0.1:
            self.speed = self.speed - self.speed / 25
        else:
            self.speed = 0.0

    def check_striker_collision(self, striker):
        if pygame.sprite.collide_mask(striker, self):
            col_x, col_y = pygame.sprite.collide_mask(striker, self)
            dx = col_x - self.mask.get_rect().centerx
            dy = col_y - self.mask.get_rect().centery
            self.col_angle_rads = math.atan2(dy, dx)
            self.speed += striker.speed

    def move_to_board(self, board_rect):
        if self.rect.x + self.rect.width > board_rect.x + board_rect.width:
            self.rect.x = board_rect.x + board_rect.width - self.rect.width
        elif self.rect.x < board_rect.x:
            self.rect.x = board_rect.x
        if self.rect.y + self.rect.height > board_rect.y + board_rect.height:
            self.rect.y = board_rect.y + board_rect.height - self.rect.height
        elif self.rect.y < board_rect.y:
            self.rect.y = board_rect.y

    def check_wall_collision(self, board_rect):
        if not board_rect.contains(self.rect):
            self.move_to_board(board_rect)
            self.reverse_angle()

    def update_pos(self):
        new_x = self.rect.centerx + (self.speed * math.cos(self.col_angle_rads))
        new_y = self.rect.centery + (self.speed * math.sin(self.col_angle_rads))
        self.rect.center = new_x, new_y
