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

    def synchronise_with_server_loop(self):
        while not self.input.quit:
            x, y = self.game.player_striker.get_position()
            p_x, p_y = self.game.puck.get_position()
            has_collided = False
            if pygame.sprite.collide_mask(self.game.player_striker, self.game.puck):
                has_collided = True
            self.connection_handler.send_message(Player(x, y, p_x, p_y, has_collided))
            enemy = self.connection_handler.receive_message_from_server()
            if enemy is not None:
                if enemy.p_x is not None and enemy.p_y is not None:
                    self.game.puck.set_position((enemy.p_x, enemy.p_y))
                self.game.enemy_striker.set_position((enemy.x, enemy.y))

    def quit(self):
        self.connection_handler.disconnect()
