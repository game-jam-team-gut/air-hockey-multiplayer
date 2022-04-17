import config


class Striker:
    def __init__(self, img, y):
        self.img = img
        self.x = config.WINDOW_WIDTH / 2 - self.img.get_width() / 2
        self.y = y

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
