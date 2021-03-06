import pickle
import socket

import server.config as c
import shared.config as sc
from shared.player import Player


class Server:
    def __init__(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', sc.SERVER_PORT))
        self.players = [Player(), Player()]
        self.connected_addresses = []
        self.primary_sync_player_id = 1

    def accept_connection(self, addr):
        self.socket.sendto(pickle.dumps(len(self.connected_addresses)), addr)  # send ID to client
        self.connected_addresses.append(addr)
        print("Client connected " + str(addr))

    def remove_connected(self, addr):
        client_id = self.connected_addresses.index(addr)
        self.players[client_id] = Player()  # reset position when disconnected
        self.connected_addresses.remove(addr)
        print("Client disconnected " + str(addr))

    def loop(self):
        data, addr = self.socket.recvfrom(sc.PACKET_SIZE)
        if addr in self.connected_addresses:  # already connected
            data = pickle.loads(data)
            match data:
                case "disconnect":
                    self.remove_connected(addr)
                    return
                case "connect":
                    return
            self.handle_client(addr, data)
            return
        match pickle.loads(data):
            case "connect":
                self.accept_connection(addr)
            case "can_i_connect":
                if len(self.connected_addresses) < 2:
                    self.socket.sendto(pickle.dumps(True), addr)
                else:
                    self.socket.sendto(pickle.dumps(False), addr)

    def handle_client(self, addr, data):
        client_id = self.connected_addresses.index(addr)
        self.players[client_id] = data
        if self.players[client_id - 1].is_primary_sync:
            self.primary_sync_player_id = client_id
        if self.primary_sync_player_id == client_id:
            self.socket.sendto(pickle.dumps(self.players[client_id - 1].primary_map_to_enemy_side()), addr)
        else:
            self.socket.sendto(pickle.dumps(self.players[client_id - 1].secondary_map_to_enemy_side()), addr)


if __name__ == "__main__":
    server = Server()
    print("Starting UDP server on %s:%d" % sc.SERVER)
    while True:
        server.loop()
