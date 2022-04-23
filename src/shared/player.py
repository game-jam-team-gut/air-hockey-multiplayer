import shared.config

class Player:
    def __init__(self, x = shared.config.PLAYER_START_POSITION_X, 
                       y = shared.config.PLAYER_START_POSITION_Y) -> None:
        self.x = x;
        self.y = y;
    
    def map_to_enemy_side(self):
        return Player(shared.config.BOARD_WIDTH - self.x, shared.config.BOARD_HEIGHT - self.y)