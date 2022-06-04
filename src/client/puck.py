import pygame
from pymunk import Vec2d
import math

import shared.config as sc
from client.physics_game_object import PhysicsGameObject

MASS = 1
ELASTICITY = 0.999


class Puck(PhysicsGameObject):
    def __init__(self, img):
        super().__init__(img, sc.WINDOW_WIDTH / 2, sc.WINDOW_HEIGHT / 2, MASS, ELASTICITY)

    def check_collision(self, collider):
        if pygame.sprite.collide_mask(collider, self):
            col_x, col_y = pygame.sprite.collide_mask(collider, self)
            # TODO remove magic number 110
            impulse = Vec2d(-math.cos(col_x * math.pi / 110), -math.cos(col_y * math.pi / 110))
            self.body.apply_impulse_at_local_point(impulse * 5 * collider.velocity, (0, 0))
            self.rect.center = self.body.position

    def reset(self):
        self.set_position((sc.WINDOW_WIDTH / 2, sc.WINDOW_HEIGHT / 2))
        self.body.velocity = Vec2d(0.0, 0.0)

    def check_goal(self, scores):
        if self.get_position()[1] <= 0:
            scores.player_score += 1
            self.reset()
