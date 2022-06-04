class UI:
    def __init__(self, window, input) -> None:
        self.window = window
        self.input = input
        self.items = []
    
    def register(self, item):
        self.items.append(item)
    
    def update(self):
        for item in self.items:
            if item.visible:
                item.update(self.input)
                item.draw(self.window)