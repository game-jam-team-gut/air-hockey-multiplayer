import pygame

from client.ui.ui_item import UIItem
import client.ui.utils as utils

class Button(UIItem):
    def __init__(self, text, x, y, width, height, click_handler) -> None:
        super().__init__()
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.handler = click_handler
        self.color = utils.WHITE , utils.GRAY
        self.hover_color = utils.GRAY, utils.BLACK
        self.current_color = self.color
    
    def update(self, input):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if input.click:
                self.handler()
            self.current_color = self.hover_color
        else:
            self.current_color = self.color

    def draw(self, window):
        pygame.draw.rect(window, self.current_color[0], self.rect)
        utils.draw_text_with_center_at(self.text, None, self.current_color[1], window,
                                       self.rect.centerx, self.rect.centery)
    
    