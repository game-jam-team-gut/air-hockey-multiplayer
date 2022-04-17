import config
from app import App
from connection_handler import ConnectionHandler


def main():
    connection_handler = ConnectionHandler(config.SERVER_ADDRESS, config.SERVER_PORT)
    app = App(connection_handler)
    app.loop()


if __name__ == "__main__":
    main()
