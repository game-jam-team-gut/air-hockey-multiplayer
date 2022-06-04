from _thread import *
import pygame

from client.screens.screen import Screen
from client.game import Game
from client.input import Input
from client.connection_handler import ConnectionHandler
from client.ui.label_with_background import LabelWithBackground
from client.ui.ui import UI
from shared.player import Player
import shared.config as sc
import client.ui.utils as ui_utils


class GameScreen(Screen):
    def __init__(self, window, change_screen, server_address, server_port) -> None:
        super().__init__(window, change_screen)
        self.game = Game()
        self.input = Input()
        self.connection_handler = ConnectionHandler(server_address, server_port)
        self.connection_handler.connect()
        start_new_thread(self.send_data, ())
        start_new_thread(self.receive_data, ())

        self.UI = UI(window, self.input)
        self.player_points_label = LabelWithBackground(str(self.game.scores.player_score), sc.WINDOW_WIDTH - sc.WINDOW_WIDTH / 6,
                                                       sc.WINDOW_HEIGHT - sc.WINDOW_WIDTH / 6, sc.WINDOW_WIDTH / 6, sc.WINDOW_WIDTH / 6, (ui_utils.BLACK, ui_utils.RED))
        self.enemy_points_label = LabelWithBackground(str(self.game.scores.enemy_score), sc.WINDOW_WIDTH - sc.WINDOW_WIDTH / 6,
                                                      0, sc.WINDOW_WIDTH / 6, sc.WINDOW_WIDTH / 6, (ui_utils.BLACK, ui_utils.RED))
        self.UI.register(self.player_points_label)
        self.UI.register(self.enemy_points_label)

    def update(self, delta_time):
        self.input.handle()
        self.game.update(self.input)
        self.game.draw(self.window)
        self.player_points_label.text = str(self.game.scores.player_score)
        self.enemy_points_label.text = str(self.game.scores.enemy_score)
        self.UI.update()
        pygame.display.flip()

    def send_data(self):
        while not self.input.quit:
            s_x, s_y = self.game.player_striker.get_position()
            p_x, p_y = self.game.puck.get_position()
            p_velocity = self.game.puck.get_velocity()
            points = self.game.scores.player_score
            is_primary_sync = False
            if pygame.sprite.collide_mask(self.game.player_striker, self.game.puck) or self.game.puck.get_position()[1] <= 0:
                is_primary_sync = True
            self.connection_handler.send_message(Player(s_x, s_y, p_x, p_y, p_velocity, points, is_primary_sync))

    def receive_data(self):
        while not self.input.quit:
            enemy = self.connection_handler.receive_message_from_server()
            if enemy is not None:
                if enemy.p_x is not None and enemy.p_y is not None:
                    self.game.puck.set_position((enemy.p_x, enemy.p_y))
                if enemy.p_velocity is not None:
                    self.game.puck.set_velocity(enemy.p_velocity)
                if enemy.s_x is not None and enemy.s_y is not None:
                    self.game.enemy_striker.set_position((enemy.s_x, enemy.s_y))
                if enemy.points is not None:
                    self.game.scores.enemy_score = enemy.points
                if enemy.is_primary_sync is not None:
                    self.game.player_striker.is_primary_sync = enemy.is_primary_sync

    def quit(self):
        self.connection_handler.disconnect()
