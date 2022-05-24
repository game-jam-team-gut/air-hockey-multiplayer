import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.mask = pygame.mask.from_surface(self.image)
