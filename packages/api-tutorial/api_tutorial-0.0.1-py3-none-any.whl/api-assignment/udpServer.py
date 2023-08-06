#!/usr/bin/env python3

# API to implement a server that communicates with clients 
# using the UDP Internet protocol
import socketserver

# Server side
class UDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """
    def handle(self):
        # Process incoming client request
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    with socketserver.UDPServer((HOST, PORT), UDPHandler) as server:
        try:
            server.serve_forever() # Activate the server
        except KeyboardInterrupt: #CTRL-C
            print("Server interrupted by user")
        finally:
            server.shutdown()

