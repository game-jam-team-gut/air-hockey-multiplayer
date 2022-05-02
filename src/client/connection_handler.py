import socket
import pickle

import client.config as c
import shared.config as sc


class ConnectionHandler:
    def __init__(self, server_address, server_port) -> None:
        self.server_address = server_address
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(c.REQUEST_TIMEOUT)
        self.id = None

    def connect(self):
        self._send_message("connect")
        self.id = pickle.loads(self.socket.recv(sc.PACKET_SIZE))
        print("Connected to server, my ID: " + str(self.id))

    def disconnect(self):
        self._send_message("disconnect")
        self.id = None
        print("Connected from server")

    def _send_message(self, data):
        for _ in range(sc.PACKET_SEND_REPEAT_COUNT):
            try:
                self.socket.sendto(pickle.dumps(data), (self.server_address, self.server_port))
            except socket.error as e:
                print(e)

    def send_message(self, data):
        if self.id is None:
            print("Error: not connected to server " + str(self.id))
            return
        self._send_message(data)

    def receive_message_from_server(self):
        if self.id is None:
            print("Error: not connected to server")
            return
        try:
            return pickle.loads(self.socket.recv(sc.PACKET_SIZE))
        except socket.timeout:
            print('Error: request timed out!')
            return None
