import shared.config as sc


class Player:
    def __init__(self, x=sc.PLAYER_START_X, y=sc.PLAYER_START_Y, speed=0.0) -> None:
        self.x = x
        self.y = y
        self.speed = speed

    def map_to_enemy_side(self):
        return Player(sc.WINDOW_WIDTH - self.x, sc.WINDOW_HEIGHT - self.y, self.speed)
