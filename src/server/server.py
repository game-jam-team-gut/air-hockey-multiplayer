import asyncio

import config


class EchoServerProtocol:
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        print(transport)

    def datagram_received(self, data, address):
        message = data.decode()
        print('Received %r from %s' % (message, address))
        print('Send %r to %s' % (message, address))
        self.transport.sendto(data, address)


def main():
    print("Starting UDP server on %s:%d" % config.ADDRESS)

    loop = asyncio.get_event_loop_policy().get_event_loop()

    listen = loop.create_datagram_endpoint(lambda: EchoServerProtocol(), local_addr=config.ADDRESS)
    transport, protocol = loop.run_until_complete(listen)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    transport.close()
    loop.close()


if __name__ == "__main__":
    main()
