import pygame
from client.scores import Scores
import pymunk
import pymunk.pygame_util

import shared.config as sc
from client.asset_manager import AssetManager
from client.board import Board
from client.play_area import PlayArea
from client.striker import Striker
from client.puck import Puck


class Game:
    def __init__(self) -> None:
        self.space = pymunk.Space()

        self.asset_manager = AssetManager()

        self.board = Board(self.asset_manager.scale_img(self.asset_manager.board_img))

        self.play_area = PlayArea(self.asset_manager.scale_img(self.asset_manager.play_area_img), self.space)
        self.space.add(*self.play_area.walls)

        self.player_striker, self.enemy_striker = self.init_strikers()
        self.space.add(self.player_striker.body, self.player_striker.shape)
        self.space.add(self.enemy_striker.body, self.enemy_striker.shape)

        self.puck = Puck(self.asset_manager.scale_img(self.asset_manager.puck_img))
        self.space.add(self.puck.body, self.puck.shape)

        self.scores = Scores()

    def init_strikers(self):
        player_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img),
                                 sc.PLAYER_STRIKER_START_Y)
        enemy_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img), sc.ENEMY_STRIKER_START_Y)
        return player_striker, enemy_striker

    def draw(self, window):
        window.fill((255, 255, 255))
        group = pygame.sprite.RenderPlain()
        group.add(self.board)
        group.add(self.player_striker)
        group.add(self.enemy_striker)
        group.add(self.puck)
        group.draw(window)
        # debug body drawing
        # draw_options = pymunk.pygame_util.DrawOptions(window)
        # self.space.debug_draw(draw_options)

    def update_physics(self):
        time_step = 1 / 60
        self.space.step(time_step)

    def update(self, player_input):
        self.update_physics()

        self.player_striker.check_player_input(player_input, self.play_area.player_movement_area)
        self.player_striker.synchronise_pos()

        self.puck.check_collision(self.player_striker)
        self.puck.check_goal(self.scores)
        if self.player_striker.is_primary_sync:
            self.puck.synchronise_pos()
