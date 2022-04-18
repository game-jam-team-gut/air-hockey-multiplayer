import pygame

LEFT = 1


class Input:
    def __init__(self) -> None:
        self.quit = False
        self.dragging = False

    def handle(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.quit = True
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == LEFT:
                        self.dragging = True
                case pygame.MOUSEBUTTONUP:
                    if event.button == LEFT:
                        self.dragging = False
