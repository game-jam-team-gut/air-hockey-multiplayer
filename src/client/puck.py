import pygame
import pymunk
from pymunk import Vec2d

import shared.config as sc
from client.game_object import GameObject


class Puck(pygame.sprite.Sprite, GameObject):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (sc.WINDOW_WIDTH / 2, sc.WINDOW_HEIGHT / 2)
        self.mask = pygame.mask.from_surface(self.image)

        mass = 1
        moment = pymunk.moment_for_circle(mass, 0, self.rect.width, (0, 0))
        self.body = pymunk.Body(mass, moment)
        self.body.position = self.rect.centerx, self.rect.centery
        self.shape = pymunk.Circle(self.body, self.rect.width / 2, (0, 0))
        self.shape.elasticity = 1

    def update_pos(self, player_striker, enemy_striker):
        if pygame.sprite.collide_mask(player_striker, self):
            self.body.apply_impulse_at_local_point(Vec2d.unit() * -200, (0, 0))
        if pygame.sprite.collide_mask(enemy_striker, self):
            self.body.apply_impulse_at_local_point(Vec2d.unit() * 200, (0, 0))
        self.rect.center = self.body.position.x, self.body.position.y
