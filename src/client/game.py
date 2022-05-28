import pygame
import pymunk
import pymunk.pygame_util

import shared.config as sc
from client.asset_manager import AssetManager
from client.board import Board
from client.score import Score
from client.time import Time
from client.striker import Striker
from client.puck import Puck


class Game:
    def __init__(self) -> None:
        self.space = pymunk.Space()

        self.asset_manager = AssetManager()

        self.board = Board(self.asset_manager.scale_img(self.asset_manager.board_img), self.space)
        self.space.add(*self.board.walls)

        self.player_score, self.enemy_score, self.time = self.init_user_interface()

        self.player_striker, self.enemy_striker = self.init_strikers()
        self.space.add(self.player_striker.body, self.player_striker.shape)
        self.space.add(self.enemy_striker.body, self.enemy_striker.shape)

        self.puck = Puck(self.asset_manager.scale_img(self.asset_manager.puck_img))
        self.space.add(self.puck.body, self.puck.shape)

    def init_user_interface(self):
        scaled_ui_bg_big_img = self.asset_manager.scale_img(self.asset_manager.result_bg_big_img)
        player_score = Score(scaled_ui_bg_big_img, sc.WINDOW_WIDTH - scaled_ui_bg_big_img.get_width() / 2,
                             sc.WINDOW_HEIGHT - scaled_ui_bg_big_img.get_height() / 2)
        enemy_score = Score(scaled_ui_bg_big_img, sc.WINDOW_WIDTH - scaled_ui_bg_big_img.get_width() / 2,
                            scaled_ui_bg_big_img.get_height() / 2)
        time = Time(scaled_ui_bg_big_img, scaled_ui_bg_big_img.get_width() / 2, sc.WINDOW_HEIGHT / 2)
        return player_score, enemy_score, time

    def init_strikers(self):
        player_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img), sc.PLAYER_STRIKER_START_Y)
        enemy_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img), sc.ENEMY_STRIKER_START_Y)
        return player_striker, enemy_striker

    def draw(self, window):
        window.fill((255, 255, 255))
        group = pygame.sprite.RenderPlain()
        group.add(self.board)
        group.add(self.player_score)
        group.add(self.enemy_score)
        group.add(self.time)
        group.add(self.player_striker)
        group.add(self.enemy_striker)
        group.add(self.puck)
        group.draw(window)
        # debug body drawing
        # draw_options = pymunk.pygame_util.DrawOptions(window)
        # self.space.debug_draw(draw_options)
        pygame.display.flip()

    def update_physics(self):
        time_step = 0.02
        self.space.step(time_step)

    def update(self, player_input):
        self.update_physics()

        self.player_striker.check_player_input(player_input, self.board.player_striker_movement_area)
        self.player_striker.synchronise_pos()

        self.puck.check_collision(self.player_striker)
        if self.player_striker.is_primary_sync:
            self.puck.synchronise_pos()
