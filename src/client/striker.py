import client.config as c


class Striker:
    def __init__(self, img, y):
        self.img = img
        self.x = c.WINDOW_WIDTH / 2 - self.img.get_width() / 2
        self.y = y

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
