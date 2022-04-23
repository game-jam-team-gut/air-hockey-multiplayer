import pygame
from _thread import *

import client.config as c
from client.screens.game_screen import GameScreen
from client.screens.menu_screen import MenuScreen


class App:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.window = pygame.display.set_mode((int(c.WINDOW_WIDTH), int(c.WINDOW_HEIGHT)))
        pygame.display.set_caption(c.WINDOW_TITLE)

        self.clock = pygame.time.Clock()
        self.current_screen = MenuScreen(self.window, self.change_screen)

    def loop(self):
        while not self.current_screen.input.quit:
            delta_time = self.clock.tick(c.TARGET_FPS) / 1000.0
            self.current_screen.update(delta_time)
            pygame.display.update()
        self.current_screen.quit()
        pygame.quit()
    
    def change_screen(self, new_screen):
        self.current_screen = new_screen
