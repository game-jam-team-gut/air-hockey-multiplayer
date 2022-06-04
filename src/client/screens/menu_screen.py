import socket
import time
from _thread import *
from client.connection_handler import ConnectionHandler

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
        self.error_label = Label("", sc.WINDOW_WIDTH / 2 - sc.WINDOW_WIDTH / 4, sc.WINDOW_HEIGHT / 2 - 100, ui_utils.RED)
        self.error_label.visible = False
        self.UI.register(self.ip_input)
        self.UI.register(Button("Connect", sc.WINDOW_WIDTH / 2 - sc.WINDOW_WIDTH / 6, sc.WINDOW_HEIGHT / 2 + 50, sc.WINDOW_WIDTH / 3, 50,
                         self.validate_ip))
        self.UI.register(self.error_label)
    
    def validate_ip(self):
        if self.ip_input.value == "":
            self.ip_input.value = "127.0.0.1"
        try:
            socket.inet_aton(self.ip_input.value)
        except:
            start_new_thread(self.show_error, ("Wrong server address.",))
            return
        
        connection_handler = ConnectionHandler(self.ip_input.value, sc.SERVER_PORT)
        can = connection_handler.can_connect()
        if can == None:
            start_new_thread(self.show_error, ("No server running on provided address.",))
            return
        
        if can == False:
            start_new_thread(self.show_error, ("Server is full.",))
            return

        self.change_screen(GameScreen(self.window, self.change_screen, self.ip_input.value, sc.SERVER_PORT))
    
    def show_error(self, error_text):
        self.error_label.visible = True
        self.error_label.text = error_text
        time.sleep(2)
        self.error_label.visible = False

    def update(self, delta_time):
        self.window.fill(ui_utils.BLACK)
        self.input.handle()
        self.UI.update()

    def quit(self):
        pass
