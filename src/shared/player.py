import shared.config as sc


class Player:
    def __init__(self, s_x=sc.PLAYER_START_X, s_y=sc.PLAYER_START_Y, p_x=sc.WINDOW_WIDTH / 2, p_y=sc.WINDOW_HEIGHT / 2,
                 p_velocity=0.0, has_collided=False) -> None:
        self.s_x = s_x
        self.s_y = s_y
        self.p_x = p_x
        self.p_y = p_y
        self.p_velocity = p_velocity
        self.has_collided = has_collided

    def primary_map_to_enemy_side(self):
        return Player(sc.WINDOW_WIDTH - self.s_x, sc.WINDOW_HEIGHT - self.s_y,
                      sc.WINDOW_WIDTH - self.p_x, sc.WINDOW_HEIGHT - self.p_y, self.p_velocity, self.has_collided)

    def secondary_map_to_enemy_side(self):
        return Player(sc.WINDOW_WIDTH - self.s_x, sc.WINDOW_HEIGHT - self.s_y, None, None, None, self.has_collided)
