import pygame

LEFT = 1


class Input:
    def __init__(self) -> None:
        self.quit = False
        self.dragging = False
        self.click = False
        self.backspace = False
        self.enter = False
        self.unicode = ""

    def handle(self):
        self.click = False
        self.backspace = False
        self.unicode = ""
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.quit = True
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == LEFT:
                        self.dragging = True
                        self.click = True
                case pygame.MOUSEBUTTONUP:
                    if event.button == LEFT:
                        self.dragging = False
                case pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.backspace = True
                    elif event.key == pygame.K_RETURN:
                        self.enter = True
                    else:
                        self.unicode += event.unicode
