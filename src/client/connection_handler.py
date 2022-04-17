import socket

import client.config as c


class ConnectionHandler:
    def __init__(self, server_address, server_port) -> None:
        self.server_address = server_address
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(c.REQUEST_TIMEOUT)

    def send_message(self, message):
        self.socket.sendto(message.encode(), (self.server_address, self.server_port))

    def receive_message_from_server(self):
        try:
            data, server = self.socket.recvfrom(c.PACKET_SIZE)
            return data.decode()
        except socket.timeout:
            print('Error: request timed out!')
            return None
