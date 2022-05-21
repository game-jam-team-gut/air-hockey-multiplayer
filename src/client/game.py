import pygame
import pymunk
import pymunk.pygame_util

import shared.config as sc
from client.asset_manager import AssetManager
from client.board import Board
from client.striker import Striker
from client.puck import Puck


class Game:
    def __init__(self) -> None:
        self.space = pymunk.Space()

        self.asset_manager = AssetManager()
        self.board = Board(self.asset_manager.scale_img(self.asset_manager.board_img))
        walls = [
            pymunk.Segment(self.space.static_body, (self.board.rect.x, self.board.rect.y),
                           (self.board.rect.x + self.board.rect.width, self.board.rect.y), 1.0),
            pymunk.Segment(self.space.static_body, (self.board.rect.x, self.board.rect.y + self.board.rect.height),
                           (self.board.rect.x + self.board.rect.width, self.board.rect.y + self.board.rect.height),
                           1.0),
            pymunk.Segment(self.space.static_body, (self.board.rect.x, self.board.rect.y),
                           (self.board.rect.x, self.board.rect.y + self.board.rect.height), 1.0),
            pymunk.Segment(self.space.static_body, (self.board.rect.x + self.board.rect.width, self.board.rect.y),
                           (self.board.rect.x + self.board.rect.width, self.board.rect.y + self.board.rect.height),
                           1.0)
        ]
        for wall in walls:
            wall.elasticity = 0.75
            wall.group = 1
        self.space.add(*walls)

        player_start_y = sc.WINDOW_HEIGHT - self.asset_manager.striker_img.get_height() / 2
        self.player_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img), player_start_y)
        self.space.add(self.player_striker.body, self.player_striker.shape)

        enemy_start_y = self.asset_manager.striker_img.get_height() / 2
        self.enemy_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img), enemy_start_y)
        self.space.add(self.enemy_striker.body, self.enemy_striker.shape)

        self.puck = Puck(self.asset_manager.scale_img(self.asset_manager.puck_img))
        self.space.add(self.puck.body, self.puck.shape)

    def draw(self, window):
        window.fill((255, 255, 255))
        group = pygame.sprite.RenderPlain()
        group.add(self.board)
        group.add(self.player_striker)
        group.add(self.enemy_striker)
        group.add(self.puck)
        group.draw(window)
        draw_options = pymunk.pygame_util.DrawOptions(window)
        self.space.debug_draw(draw_options)
        pygame.display.flip()

    def update_physics(self):
        time_step = 0.02
        self.space.step(time_step)

    def update(self, player_input):
        self.update_physics()
        self.player_striker.update_pos(player_input, self.board.rect)
        self.enemy_striker.update_body_pos()
        self.puck.update_pos(self.player_striker, self.enemy_striker)
