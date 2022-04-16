from app import App
from connection_handler import ConnectionHandler
import config


def main():
    connection_handl = ConnectionHandler(config.SERVER_ADDRESS, config.SERVER_PORT)
    app = App(connection_handl)
    app.loop()


if __name__ == "__main__":
    main()
