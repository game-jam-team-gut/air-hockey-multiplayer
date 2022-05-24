from _thread import *
import pygame

from client.screens.screen import Screen
from client.game import Game
from client.input import Input
from client.connection_handler import ConnectionHandler
from shared.player import Player
import shared.config as sc


class GameScreen(Screen):
    def __init__(self, window, change_screen) -> None:
        super().__init__(window, change_screen)
        self.game = Game()
        self.input = Input()
        self.connection_handler = ConnectionHandler(sc.SERVER_ADDRESS, sc.SERVER_PORT)
        self.connection_handler.connect()
        start_new_thread(self.synchronise_with_server_loop, ())

    def update(self, delta_time):
        self.input.handle()
        self.game.update(self.input)
        self.game.draw(self.window)

    def synchronise_all_uninterruptable(self, x, y):
        self.game.player_striker.sync_flag = True
        p_x, p_y = self.game.puck.get_position()
        self.connection_handler.send_message(Player(x, y, p_x, p_y, self.game.player_striker.sync_flag))
        enemy = self.connection_handler.receive_message_from_server()
        if enemy is not None:
            self.game.enemy_striker.set_position((enemy.x, enemy.y))
        else:
            print("Cannot get data from server!")

    def synchronise_all_interruptable(self, x, y):
        p_x, p_y = self.game.puck.get_position()
        self.connection_handler.send_message(Player(x, y, p_x, p_y))
        enemy = self.connection_handler.receive_message_from_server()
        if enemy is not None:
            if enemy.sync_flag is not None:
                self.game.player_striker.sync_flag = False
            self.game.enemy_striker.set_position((enemy.x, enemy.y))
        else:
            print("Cannot get data from server!")

    def synchronise_striker(self, x, y):
        self.connection_handler.send_message(Player(x, y))
        enemy = self.connection_handler.receive_message_from_server()
        if enemy is not None:
            if enemy.p_x is not None and enemy.p_y is not None:
                self.game.puck.set_position((enemy.p_x, enemy.p_y))
            if enemy.sync_flag is not None:
                self.game.player_striker.sync_flag = False
            self.game.enemy_striker.set_position((enemy.x, enemy.y))
        else:
            print("Cannot get data from server!")

    def synchronise_with_server_loop(self):
        while not self.input.quit:
            x, y = self.game.player_striker.get_position()
            if pygame.sprite.collide_mask(self.game.player_striker, self.game.puck):
                self.synchronise_all_uninterruptable(x, y)
            elif self.game.player_striker.sync_flag:
                self.synchronise_all_interruptable(x, y)
            else:
                self.synchronise_striker(x, y)

    def quit(self):
        self.connection_handler.disconnect()
