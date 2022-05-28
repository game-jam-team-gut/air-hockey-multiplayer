import pymunk

from client.game_object import GameObject


class PhysicsGameObject(GameObject):
    def __init__(self, img, x, y, mass, elasticity):
        super().__init__(img, x, y)
        self.mass = mass
        self.moment = pymunk.moment_for_circle(mass, 0, img.get_rect().width / 2, (0, 0))
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, img.get_rect().width / 2, (0, 0))
        self.shape.elasticity = elasticity

    def set_position(self, position):
        self.body.position = position
        self.rect.center = position

    def set_velocity(self, velocity):
        self.body.velocity = velocity

    def get_position(self):
        return self.body.position

    def get_velocity(self):
        return self.body.velocity

    def synchronise_pos(self):
        self.rect.center = self.body.position
