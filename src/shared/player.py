import shared.config as sc


class Player:
    def __init__(self, x=sc.PLAYER_START_X, y=sc.PLAYER_START_Y, p_x=None, p_y=None, sync_flag=None) -> None:
        self.x = x
        self.y = y
        self.p_x = p_x
        self.p_y = p_y
        self.sync_flag = sync_flag

    def map_to_enemy_side(self):
        if self.p_x is not None and self.p_y is not None:
            return Player(sc.WINDOW_WIDTH - self.x, sc.WINDOW_HEIGHT - self.y,
                          sc.WINDOW_WIDTH - self.p_x, sc.WINDOW_HEIGHT - self.p_y, self.sync_flag)
        else:
            return Player(sc.WINDOW_WIDTH - self.x, sc.WINDOW_HEIGHT - self.y, self.p_x, self.p_y, self.sync_flag)
