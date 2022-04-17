import pygame

import config
from game import Game


class App:

    def __init__(self, connection_handler):
        self.quit = False

        pygame.init()
        pygame.font.init()

        self.window = pygame.display.set_mode(
            (int(config.WINDOW_WIDTH), int(config.WINDOW_HEIGHT)))
        pygame.display.set_caption(config.WINDOW_TITLE)

        self.clock = pygame.time.Clock()

        self.connection_handler = connection_handler
        self.game = Game()

    def loop(self):
        while not self.quit:
            self.clock.tick(config.TARGET_FPS)
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
