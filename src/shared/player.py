import shared.config as sc


class Player:
    def __init__(self, x=sc.PLAYER_START_X, y=sc.PLAYER_START_Y, p_x=sc.WINDOW_WIDTH / 2, p_y=sc.WINDOW_HEIGHT / 2,
                 has_collided=False) -> None:
        self.x = x
        self.y = y
        self.p_x = p_x
        self.p_y = p_y
        self.has_collided = has_collided

    def primary_map_to_enemy_side(self):
        return Player(sc.WINDOW_WIDTH - self.x, sc.WINDOW_HEIGHT - self.y,
                      sc.WINDOW_WIDTH - self.p_x, sc.WINDOW_HEIGHT - self.p_y, self.has_collided)

    def secondary_map_to_enemy_side(self):
        return Player(sc.WINDOW_WIDTH - self.x, sc.WINDOW_HEIGHT - self.y, None, None, self.has_collided)
