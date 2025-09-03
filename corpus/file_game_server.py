from twisted.internet import protocol, reactor
from twisted.protocols.basic import LineReceiver

class ChatProtocol(LineReceiver):
    def connectionMade(self):
        self.factory.clients.append(self)
        self.broadcast(f"{self.transport.getPeer().host} has joined the chat.")

    def connectionLost(self, reason):
        self.factory.clients.remove(self)
        self.broadcast(f"{self.transport.getPeer().host} has left the chat.")

    def lineReceived(self, line):
        message = line.decode('utf-8')
        self.broadcast(f"{self.transport.getPeer().host}: {message}")

    def broadcast(self, message):
        for client in self.factory.clients:
            client.sendLine(message.encode('utf-8'))

class ChatFactory(protocol.Factory):
    def __init__(self):
        self.clients = []

    def buildProtocol(self, addr):
        return ChatProtocol()

if __name__ == "__main__":
    port = 8000
    factory = ChatFactory()
    reactor.listenTCP(port, factory)
    print(f"Chat server started on port {port}")
    reactor.run()
