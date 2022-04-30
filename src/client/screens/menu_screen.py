import pygame

from client.screens.screen import Screen
from client.screens.game_screen import GameScreen
from client.input import Input


class MenuScreen(Screen):
    def __init__(self, window, change_screen) -> None:
        super().__init__(window, change_screen)
        self.input = Input()

    def update(self, delta_time):
        self.input.handle()
        textobj = pygame.font.SysFont(None, 50).render("Main menu", 1, (255, 255, 255))
        textrect = textobj.get_rect()
        textrect.topleft = (20, 20)
        self.window.blit(textobj, textrect)
        if self.input.dragging:
            self.change_screen(GameScreen(self.window, self.change_screen))

    def quit(self):
        pass
