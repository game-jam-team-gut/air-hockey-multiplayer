import pygame
from math import sqrt, atan2

import client.config as c
from client.asset_manager import AssetManager
from client.board import Board
from client.striker import Striker
from client.puck import Puck

WHITE = 255, 255, 255


class Game:
    def __init__(self) -> None:
        self.asset_manager = AssetManager()
        self.board = Board(self.asset_manager.scale_img(self.asset_manager.board_img))

        player_start_y = c.WINDOW_HEIGHT - self.asset_manager.striker_img.get_height() / 2
        self.player_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img), player_start_y)

        enemy_start_y = self.asset_manager.striker_img.get_height() / 2
        self.enemy_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img), enemy_start_y)

        self.puck = Puck(self.asset_manager.scale_img(self.asset_manager.puck_img))

    def check_puck_hit(self, striker):
        if pygame.sprite.collide_mask(striker, self.puck):
            # TODO: remove 55, 55 magic numbers representing x, y of centre of scaled puck
            col_x, col_y = pygame.sprite.collide_mask(striker, self.puck)
            dx = col_x - 55
            dy = col_y - 55
            self.puck.speed = striker.speed
            self.puck.col_angle_rads = atan2(dy, dx)

    def draw(self, window):
        window.fill(WHITE)
        group = pygame.sprite.RenderPlain()
        group.add(self.board)
        group.add(self.player_striker)
        group.add(self.enemy_striker)
        group.add(self.puck)
        group.draw(window)
        pygame.display.flip()

    def update(self, player_input):
        old_pos = self.player_striker.get_position()
        self.player_striker.update_pos(player_input)
        new_pos = self.player_striker.get_position()
        self.player_striker.speed = sqrt((old_pos[0] - new_pos[0])**2 + (old_pos[1] - new_pos[1])**2)

        self.check_puck_hit(self.player_striker)
        self.check_puck_hit(self.enemy_striker)
        self.puck.update_pos()
        self.puck.slow_down()
