from abc import ABC, abstractmethod

class UIItem(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.visible = True
    
    def hide(self):
        self.visible = False
    
    def show(self):
        self.visible = True

    @abstractmethod
    def update(self, input):
        pass

    @abstractmethod
    def draw(self, window):
        pass
