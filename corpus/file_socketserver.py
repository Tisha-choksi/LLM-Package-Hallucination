from SocketServer import TCPServer, StreamRequestHandler

class ChatHandler(StreamRequestHandler):
    def handle(self):
        print(f"Connection from: {self.client_address}")
        self.wfile.write(b"Welcome to the chat server!\n")
        while True:
            message = self.rfile.readline().strip()
            if message:
                print(f"Received: {message}")
                self.wfile.write(b"Message received\n")
            else:
                break

if __name__ == "__main__":
    server = TCPServer(('localhost', 9999), ChatHandler)
    print("Chat server running on port 9999...")
    server.serve_forever()