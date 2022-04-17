import pygame

import client.config as c
from client.asset_manager import AssetManager
from client.board import Board
from client.striker import Striker
from client.puck import Puck


class Game:
    def __init__(self) -> None:
        self.asset_manager = AssetManager()
        self.board = Board(self.asset_manager.scale_img(self.asset_manager.board_img))
        self.player_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img),
                                      c.WINDOW_HEIGHT - self.asset_manager.striker_img.get_height() / 2)
        self.enemy_striker = Striker(self.asset_manager.scale_img(self.asset_manager.striker_img),
                                     self.asset_manager.striker_img.get_height() / 2)
        self.puck = Puck(self.asset_manager.scale_img(self.asset_manager.puck_img))

    def draw(self, window):
        window.fill((255, 255, 255))
        group = pygame.sprite.RenderPlain()
        group.add(self.board)
        group.add(self.player_striker)
        group.add(self.enemy_striker)
        group.add(self.puck)
        group.draw(window)
        pygame.display.flip()

    def update(self, input):
        mouse_pos = pygame.mouse.get_pos()
        if input.dragging:
            if self.player_striker.dragged:
                self.player_striker.set_position(mouse_pos)
            elif self.player_striker.rect.collidepoint(mouse_pos):
                self.player_striker.set_position(mouse_pos)
                self.player_striker.dragged = True
        else:
            self.player_striker.dragged = False
