from client.game_object import GameObject


class Scoreboard(GameObject):
    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        self.points = 0
