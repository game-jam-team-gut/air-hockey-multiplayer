import pygame
from math import atan2

import shared.config as sc
from client.asset_manager import AssetManager
from client.board import Board
from client.striker import Striker
from client.puck import Puck


class Game:
    def __init__(self) -> None:
        self.asset_manager = AssetManager()
        self.board = Board(self.asset_manager.scale_img(self.asset_manager.board_img))

        player_start_y = sc.WINDOW_HEIGHT - self.asset_manager.striker_img.get_height() / 2
        self.player_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img),
                                      player_start_y, self.board.rect)

        enemy_start_y = self.asset_manager.striker_img.get_height() / 2
        self.enemy_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img),
                                     enemy_start_y, self.board.rect)

        self.puck = Puck(self.asset_manager.scale_img(self.asset_manager.puck_img))

    def draw(self, window):
        window.fill((255, 255, 255))
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
        self.player_striker.update_speed(old_pos)

        self.puck.slow_down()
        self.puck.check_striker_collision(self.player_striker)
        self.puck.check_striker_collision(self.enemy_striker)
        self.puck.check_wall_collision(self.board.rect)
        self.puck.update_pos()
