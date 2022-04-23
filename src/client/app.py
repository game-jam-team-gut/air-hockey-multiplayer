import pygame

import client.config as c
from client.game import Game
from client.input import Input
from shared.player import Player


class App:
    def __init__(self, connection_handler):
        pygame.init()
        pygame.font.init()

        self.window = pygame.display.set_mode((int(c.WINDOW_WIDTH), int(c.WINDOW_HEIGHT)))
        pygame.display.set_caption(c.WINDOW_TITLE)

        self.clock = pygame.time.Clock()

        self.connection_handler = connection_handler
        self.game = Game()
        self.player_input = Input()

    def loop(self):
        while not self.player_input.quit:
            self.clock.tick(c.TARGET_FPS)

            self.player_input.handle()
            self.game.update(self.player_input)

            self.synchronise_with_server()

            self.game.draw(self.window)
            pygame.display.update()
        self.connection_handler.disconnect()
        pygame.quit()
    
    def synchronise_with_server(self):
        x, y = self.game.player_striker.get_position()
        self.connection_handler.send_message(Player(x, y))
        enemy = self.connection_handler.receive_message_from_server()
        if enemy != None:
            self.game.enemy_striker.set_position((enemy.x, enemy.y))
        else:
            print("Cannot get data from server!")
