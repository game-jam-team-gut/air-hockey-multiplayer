from client.game_object import GameObject


class Time(GameObject):
    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        self.from_start = 0.0
