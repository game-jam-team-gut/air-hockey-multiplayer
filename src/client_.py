import client.config as c
import shared.config
from client.app import App
from client.connection_handler import ConnectionHandler


def main():
    connection_handler = ConnectionHandler(shared.config.SERVER_ADDRESS, shared.config.SERVER_PORT)
    app = App(connection_handler)
    app.loop()


if __name__ == "__main__":
    main()
