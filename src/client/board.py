import config


class Board:
    def __init__(self, img):
        self.img = img
        self.size_x, self.size_y = self.img.get_size()

    def draw(self, window):
        window.blit(self.img, (config.WINDOW_WIDTH / 2 - self.size_x / 2, 0))

    img = None
    size_x = None
    size_y = None
