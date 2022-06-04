import socket
import time
from _thread import *

from client.screens.screen import Screen
from client.screens.game_screen import GameScreen
from client.input import Input
from client.ui.ui import UI
from client.ui.button import Button
from client.ui.text_input import TextInput
from client.ui.label import Label
import shared.config as sc
import client.ui.utils as ui_utils


class MenuScreen(Screen):
    def __init__(self, window, change_screen) -> None:
        super().__init__(window, change_screen)
        self.input = Input()
        self.UI = UI(window, self.input)
        self.ip_input = TextInput(sc.WINDOW_WIDTH / 2 - sc.WINDOW_WIDTH / 4, sc.WINDOW_HEIGHT / 2 - 25, sc.WINDOW_WIDTH / 2, 50)
        self.ip_error = Label("Wrong server address", sc.WINDOW_WIDTH / 2 - sc.WINDOW_WIDTH / 4, sc.WINDOW_HEIGHT / 2 - 100, ui_utils.RED)
        self.ip_error.visible = False
        self.UI.register(self.ip_input)
        self.UI.register(Button("Connect", sc.WINDOW_WIDTH / 2 - sc.WINDOW_WIDTH / 6, sc.WINDOW_HEIGHT / 2 + 50, sc.WINDOW_WIDTH / 3, 50,
                         self.validate_ip))
        self.UI.register(self.ip_error)
    
    def validate_ip(self):
        try:
            socket.inet_aton(self.ip_input.value)
        except:
            start_new_thread(self.show_wrong_ip_error, ())
            return
        self.change_screen(GameScreen(self.window, self.change_screen, self.ip_input.value, sc.SERVER_PORT))
    
    def show_wrong_ip_error(self):
        self.ip_error.visible = True
        time.sleep(2)
        self.ip_error.visible = False

    def update(self, delta_time):
        self.window.fill(ui_utils.BLACK)
        self.input.handle()
        self.UI.update()

    def quit(self):
        pass
