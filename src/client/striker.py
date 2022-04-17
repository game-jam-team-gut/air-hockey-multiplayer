import config


class Striker:
    def __init__(self, img, x, y):
        self.img = img
        self.x = x
        self.y = y
        self.size_x, self.size_y = self.img.get_size()

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    img = None
    x = None
    y = None
    size_x = None
    size_y = None
