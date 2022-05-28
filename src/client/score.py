from client.game_object import GameObject


class Score(GameObject):
    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        self.points = 0
