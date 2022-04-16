import asyncio

import config

class EchoServerProtocol:
    def connection_made(self, transport):
        self.transport = transport
        print(transport)

    def datagram_received(self, data, addr):
        message = data.decode()
        print('Received %r from %s' % (message, addr))
        print('Send %r to %s' % (message, addr))
        self.transport.sendto(data, addr)

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