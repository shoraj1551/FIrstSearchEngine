import argparse
import socket
import sys
import re

class SearchServer:
    """A very simple HTTP search server"""
    def __init__(self, port):
        self.port = port

    def run(self):
        """Run the server loop: Create a socket and then,
        in an infinte loop, wait for requests and search and
        return appropriate information for them"""

        #create server socket using IPv4 address and TCP
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Allow re-use of port if we start again after a crash
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #give address of machine and port we want to listen for connections
        server_address = ("0.0.0.0", self.port)
        server_socket.bind(server_address)

        #start listening
        server_socket.listen()

        #server loop: wait for requests and process them
        while True:
            #Wait for incoming requests
            print()
            print(f"Waiting for incoming request on port {self.port}....")
            (client_socket, client_address) = server_socket.accept()
            print(f"Received request from {client_address}")

            #read bytes from client in rounds
            request = b""
            while request.find(b"\r\r\r\n") == -1:
                request += client_socket.recv(1024)
            request = request.decode("utf-8")
            print(f"Request was {request}")

            #We are only interested in the first line and part after the 
            #GET/ and befoe the HTTP/1.1
            request = request.split("\r\n")[0]
            request = request.split(" ")[1]
            request = request.split("HTTP")[0]
            request = request.replace("/", " ")
            print(f"Request part after GET/ was: {request}")

            #Handel Requests
            response = self.handle_request(request)

            #send the response
            client_socket.sendall(response)

            #close the connection
            client_socket.close()

    def handle_request(self, request):
        """handle the request and return a suitable response"""
        #Defualt status code and Media type
        status_code = "200 OK"
        media_type = "text/plane"

        #check if the request enclose with a query string of the form ?query=
        pos = request.find("?query=")
        if pos != -1:
            query = request[pos + len("?query=")]
            request = request[0:pos]

            #simple URL decoding of query
            query = query.replace("+", " ")
            query = query.replace("%2B", "+")

            print(f"query = {query}")
        
        print(request)
        
        #interpret the request as file name
        # Try:
        #     filename = request
        



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type= int, help = "port to listen on")
    args = parser.parse_args()
    server = SearchServer(args.port)
    server.run()

if __name__ == "__main__":
    main()