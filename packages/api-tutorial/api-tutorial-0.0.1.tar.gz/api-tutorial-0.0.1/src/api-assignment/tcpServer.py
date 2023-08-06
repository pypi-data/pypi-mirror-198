#!/usr/bin/env python3

# API to implement a server that communicates with clients 
# using the TCP Internet protocol

import socketserver

# Server side
class TCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.
    """
    def handle(self):
        # receive data from client, self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        # print data
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # send back data to client (in Upper case)
        self.request.sendall(self.data.upper())

class TCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
    

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        try:
            server.serve_forever() # Activate the server
        except KeyboardInterrupt: #CTRL-C
            print("Server interrupted by user")
        finally:
            server.shutdown()