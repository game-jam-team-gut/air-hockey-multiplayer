import config


class Board:
    def __init__(self, img):
        self.img = img

    def draw(self, window):
        window.blit(self.img, (config.WINDOW_WIDTH / 2 - self.img.get_width() / 2, 0))
