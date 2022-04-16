import pygame
import socket
import time

import config
from game import Game


class App:

    def __init__(self):
        self.quit = False

        pygame.init()
        pygame.font.init()

        self.window = pygame.display.set_mode(
            (int(config.WINDOW_WIDTH), int(config.WINDOW_HEIGHT)))
        pygame.display.set_caption(config.WINDOW_TITLE)

        self.clock = pygame.time.Clock()

        self.game = Game()

    def loop(self):
        while not self.quit:
            self.clock.tick(config.TARGET_FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
            # TODO recieve input
            # TODO send to server
            # TODO get state from server and pass to update, then redraw
            self.game.update()
            self.game.draw()
                pygame.display.update()
        pygame.quit()
    
    def connect_to_server(self):
        for pings in range(10):
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client_socket.settimeout(1.0)
            message = b'test'
            addr = config.SERVER_ADDRES

            start = time.time()
            client_socket.sendto(message, addr)
            try:
                data, server = client_socket.recvfrom(1024)
                end = time.time()
                elapsed = end - start
                print(f'{data} {pings} {elapsed}')
            except socket.timeout:
                print('REQUEST TIMED OUT')
