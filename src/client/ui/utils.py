import pygame

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def draw_text(text, font, color, window, x, y):
    if font == None:
        font = pygame.font.SysFont(None, 50)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    window.blit(textobj, textrect)

def draw_text_with_center_at(text, font, color, window, x, y):
    if font == None:
        font = pygame.font.SysFont(None, 50)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=(x, y))
    window.blit(textobj, textrect)