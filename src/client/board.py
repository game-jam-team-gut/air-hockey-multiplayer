import pygame
import pymunk

import shared.config as sc
from client.game_object import GameObject


class Board(GameObject):
    def __init__(self, img, space):
        super().__init__(img, sc.WINDOW_WIDTH / 2, sc.WINDOW_HEIGHT / 2)

        self.walls = [
            pymunk.Segment(space.static_body, (self.rect.x, self.rect.y),
                           (self.rect.x + self.rect.width / 3, self.rect.y), 1.0),
            pymunk.Segment(space.static_body, (self.rect.x + self.rect.width * 2 / 3, self.rect.y),
                           (self.rect.x + self.rect.width, self.rect.y), 1.0),
            pymunk.Segment(space.static_body, (self.rect.x, self.rect.y + self.rect.height),
                           (self.rect.x + self.rect.width / 3, self.rect.y + self.rect.height), 1.0),
            pymunk.Segment(space.static_body, (self.rect.x + self.rect.width * 2 / 3, self.rect.y + self.rect.height),
                           (self.rect.x + self.rect.width, self.rect.y + self.rect.height), 1.0),
            pymunk.Segment(space.static_body, (self.rect.x, self.rect.y),
                           (self.rect.x, self.rect.y + self.rect.height), 1.0),
            pymunk.Segment(space.static_body, (self.rect.x + self.rect.width, self.rect.y),
                           (self.rect.x + self.rect.width, self.rect.y + self.rect.height), 1.0)]
        for wall in self.walls:
            wall.elasticity = 0.75
            wall.group = 1

        self.player_striker_movement_area = pygame.Rect(self.rect.x, self.rect.y + self.rect.height / 2,
                                                        self.rect.width, self.rect.height / 2)
