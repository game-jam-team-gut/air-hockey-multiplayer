import pygame

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
                        if event.button == 1:
                            self.dragging = True
                    case pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            self.dragging = False