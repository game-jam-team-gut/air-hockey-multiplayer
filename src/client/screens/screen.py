from abc import ABC, abstractmethod


class Screen(ABC):
    def __init__(self, window, change_screen) -> None:
        self.window = window
        self.change_screen = change_screen
        self.input = None

    @abstractmethod
    def update(self, delta_time):
        pass

    @abstractmethod
    def quit(self):
        pass
