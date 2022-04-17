import pygame

import client.config as c
from client.asset_manager import AssetManager
from client.board import Board
from client.striker import Striker


class Game:
    def __init__(self) -> None:
        self.asset_manager = AssetManager()
        self.board = Board(self.asset_manager.scale_img(self.asset_manager.board_img))
        self.player_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img),
                                      c.WINDOW_HEIGHT - self.asset_manager.striker_img.get_height())
        self.enemy_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img),
                                     self.asset_manager.striker_img.get_height() / 2)

    def draw(self, window):
        window.fill((255, 255, 255))
        group = pygame.sprite.RenderPlain()
        group.add(self.board)
        group.add(self.player_striker)
        group.add(self.enemy_striker)
        group.draw(window)
        pygame.display.flip()

    def update(self, input):
        mouse_pos = pygame.mouse.get_pos()
        if (input.dragging and self.player_striker.rect.collidepoint(mouse_pos)):
            self.player_striker.set_position(mouse_pos)
            # TODO dont check collidepoint, if we started dragging already, too fast mouse movements stop dragging from working
            # add additional bool variable, striker_dragging
        
