import pygame

import client.config as c
from client.game import Game


class App:

    def __init__(self, connection_handler):
        self.quit = False

        pygame.init()
        pygame.font.init()

        self.window = pygame.display.set_mode(
            (int(c.WINDOW_WIDTH), int(c.WINDOW_HEIGHT)))
        pygame.display.set_caption(c.WINDOW_TITLE)

        self.clock = pygame.time.Clock()

        self.connection_handler = connection_handler
        self.game = Game()

    def loop(self):
        while not self.quit:
            self.clock.tick(c.TARGET_FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
            # TODO receive input
            # TODO send to server
            # TODO get state from server and pass to update, then redraw
            self.game.update()
            self.game.draw(self.window)
            pygame.display.update()
        pygame.quit()
