class GameObject:
    def __init__(self):
        self.rect = None

    def set_position(self, position):
        self.rect.center = position

    def get_position(self):
        return self.rect.center
