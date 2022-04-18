import pygame

import client.config as c
from client.game import Game
from client.input import Input


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
            # TODO receive input
            # TODO send to server
            # TODO get state from server and pass to update, then redraw
            self.game.update(self.player_input)
            self.game.draw(self.window)
            pygame.display.update()
        pygame.quit()
