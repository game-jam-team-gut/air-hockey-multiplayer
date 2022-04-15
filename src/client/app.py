import pygame

import config


class App:

    def __init__(self):
        self.quit = False

        pygame.init()
        pygame.font.init()

        self.window = pygame.display.set_mode(
            (int(config.WINDOW_WIDTH), int(config.WINDOW_HEIGHT)))
        pygame.display.set_caption(config.WINDOW_TITLE)

        self.clock = pygame.time.Clock()

    def loop(self):
        while not self.quit:
            self.clock.tick(config.TARGET_FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                # update
                # draw
                pygame.display.update()
        pygame.quit()
