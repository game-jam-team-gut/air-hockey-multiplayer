from _thread import *
import pygame
import pymunk

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

    def send_data(self):
        s_x, s_y = self.game.player_striker.get_position()
        p_x, p_y = self.game.puck.get_position()
        p_velocity = self.game.puck.body.velocity
        has_collided = False
        if pygame.sprite.collide_mask(self.game.player_striker, self.game.puck):
            has_collided = True
        self.connection_handler.send_message(Player(s_x, s_y, p_x, p_y, p_velocity, has_collided))

    def receive_data(self):
        enemy = self.connection_handler.receive_message_from_server()
        if enemy.p_x is not None and enemy.p_y is not None:
            self.game.puck.set_position((enemy.p_x, enemy.p_y))
        if enemy.p_velocity is not None:
            self.game.puck.body.velocity = enemy.p_velocity
        if enemy.x is not None and enemy.y is not None:
            self.game.enemy_striker.set_position((enemy.x, enemy.y))

    def synchronise_with_server_loop(self):
        while not self.input.quit:
            self.send_data()
            self.receive_data()

    def quit(self):
        self.connection_handler.disconnect()
