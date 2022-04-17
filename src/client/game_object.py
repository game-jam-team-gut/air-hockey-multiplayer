class GameObject:
    def set_position(self, position):
        self.rect.center = position

    def get_position(self, position):
        return self.rect.center