from _thread import *

from client.screens.screen import Screen
from client.game import Game
from client.input import Input
from client.connection_handler import ConnectionHandler
from shared.player import Player
import shared.config

class GameScreen(Screen):
    def __init__(self, window, change_screen) -> None:
        super().__init__(window, change_screen)
        self.game = Game()
        self.input = Input()
        self.connection_handler = ConnectionHandler(shared.config.SERVER_ADDRESS, shared.config.SERVER_PORT)
        self.connection_handler.connect()
        start_new_thread(self.synchronise_with_server_loop, ())

    def update(self, delta_time):
        self.input.handle()
        self.game.update(self.input)
        self.game.draw(self.window)
    
    def synchronise_with_server_loop(self):
        while not self.input.quit:
            x, y = self.game.player_striker.get_position()
            self.connection_handler.send_message(Player(x, y))
            enemy = self.connection_handler.receive_message_from_server()
            if enemy != None:
                self.game.enemy_striker.set_position((enemy.x, enemy.y))
            else:
                print("Cannot get data from server!")
    
    def quit(self):
        self.connection_handler.disconnect()