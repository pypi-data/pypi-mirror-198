# 1 API to access various services via HTTP as a client. For example, downloading data or interacting with a REST-based API. use  urlib

# Import the urllib library
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from urllib.parse import urlparse, parse_qs
import http.server
import json
import cgi
import urllib
import urllib.request
import urllib.parse
import os


import tkinter as tk

import socketserver
import ipaddress


class JohnRESTServer:
    def __init__(self) -> None:
        # Create a new self.window

        self.base_url = "https://api.restful-api.dev"

    def get_data(self, endpoint='objects', param=1):

        if param is not None:
            url = self.base_url + '/' + endpoint + '/' + str(param)
        else:
            url = self.base_url + '/' + endpoint
        headers = {"User-Agent": "Mozilla/5.0",
                   "Content-Type": "application/json"}
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read().decode()
        print('get data: ', data)
        return data

        # response = requests.get(url)
        # # check if the request was successful
        # if response.status_code == 200:
        #     # retrieve the list of books from the response
        #     data = response.json()
        #     print('data', data,  endpoint, param)

        # else:
        #     # handle the error
        #     print(f"Error: {response.status_code} - {response.reason}")

    def post_data(self,  endpoint='objects', param=1, data={ 'name': 'Apple MacBook Pro 16', 'data': {
                'year': 2019, 'price': 1849.99, 'CPU model': 'Intel Core i9', 'Hard disk size': '1 TB'}}
):
        """
        to post a new id to the server"""

        import time
        created_time = time.time()
        try:
            # parse the string into a dictionary
            data['id'] = '{}'.format(param)
            data['createdAt'] = time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(created_time))
            url = os.path.join(self.base_url, endpoint)
            headers = {"User-Agent": "Mozilla/5.0",
                       "Content-Type": "application/json"}
            data = urllib.parse.urlencode(data).encode()
            req = urllib.request.Request(
                url, data=data, method="POST", headers=headers)
            response = urllib.request.urlopen(req)

            return response.read()

            # # send a POST request to create the new book
            # response = requests.post(url, json=json.dumps(data))

            # # check if the request was successful
            # if response.status_code == 201:
            #     # retrieve the ID of the new book from the response
            #     result = response.json()

            # else:
            # # handle the error
            #     print(f"Error: {response.status_code} - {response.reason}", )
        except ValueError:
            # handle the case where the string is not valid JSON
            print("Error: Invalid JSON string")

    def put_data(self,  endpoint='objects', param=1):
        url = os.path.join(self.base_url, endpoint)
        data = {'id': '{}'.format(param), "name": "Apple AirPods", "data": {
            "color": "white", "generation": "3rd", "price": 135}}
        data = urllib.parse.urlencode(data).encode()
        req = urllib.request.Request(url, data=data, method="PUT")
        response = urllib.request.urlopen(req)
        return response.read()

        # headers = {"content-type": "application/json"}
        # payload = json.dumps({'id': '{}'.format(param), "name": "Apple AirPods", "data": { "color": "white", "generation": "3rd", "price": 135}})
        # requestUrl = os.path.join(url, param)
        # r = requests.put(requestUrl, data=payload, headers=headers)

        # print(r.content)

    def delete_data(self, endpoint='objects', param=1):
        url = os.path.join(self.base_url, endpoint) + '/' + str(param)

        req = urllib.request.Request(url, method="DELETE")
        response = urllib.request.urlopen(req)
        return response.read()
        # response = requests.delete(url)

        # # check if the request was successful
        # if response.status_code == 204:
        #     # do something to indicate that the book was deleted
        #     print(f"Book with ID {param} was deleted.")
        # else:
        #     # handle the error
        #     print(f"Error: {response.status_code} - {response.reason}")


class JohnTCPServer(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the socket object
        data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]} wrote: {data}")
        # send a response back to the client
        # self.request.sendall(b"Hello, client!")
        self.request.sendall(transform_data(data))


def transform_data(data):
    return data.upper()


class JohnUDPServer(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the socket object
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        socket.sendto(data.upper(), self.client_address)


class JohnIPRange:
    def ipd4range(self, cidr):
        network = ipaddress.ip_network(cidr)
        return list(network)

    def ipd6range(self, cidr):
        network = ipaddress.ip_network(cidr)
        return list(network)


def process_command(command):
    if command == "status":
        return {"status": "ok"}
    elif command == "stop":
        return {"status": "stopped"}
    else:
        return {"status": "error", "message": "Unknown command"}

# define a request handler for incoming HTTP requests


class JohnInterfaceHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        result = urlparse(self.path)
        command = parse_qs(result.query)
        command_val = command.get("command", [''])[0]

        # process the command and generate a response
        response = process_command(command_val)
        # send the response back to the client
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


class JohnXMLRPCReqHandler(SimpleXMLRPCRequestHandler):
    pass  # Keep the class empty as it inherits from SimpleXMLRPCRequestHandler


class JohnXMLRPCRequestHandler:
    def __init__(self, url='localhost', port=8000):
        self.server = SimpleXMLRPCServer(
            (url, port), requestHandler=JohnXMLRPCReqHandler, logRequests=True, allow_none=True)
        self.server.register_function(self.add, 'add')

    def start_server(self):
        # start the server and run forever
        print("Starting server...")
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            print("Stopping server...")
            self.server.server_close()

    def add(self, x, y):
        return x + y

    def get_location(self, place_name):
        pass

import socket
import ssl
def JohnAuthenticationHandler(certfile='server.crt', keyfile='server.key', HOST='localhost', PORT=12345):
    # Create an SSL context and set the SSL/TLS protocol and cipher suite
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    # Load the certificate chain file
    ssl_context.load_verify_locations(cafile='chain.pem')

    # Listen for incoming connections and wrap them with SSL/TLS
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        with ssl_context.wrap_socket(sock, server_side=True) as ssl_sock:
            print('Server is listening...')

            # Accept incoming connections and receive data
            conn, addr = ssl_sock.accept()
            with conn:
                print(f'Connected by {addr}')
                data = conn.recv(1024)
                print(f'Received from client: {data}')

                # Send a response
                conn.sendall(b'Hello, client!')

    print('Server is shutting down...')

def ssl_client(msg, client_cert='ca.crt', host='localhost', port=12345):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(cafile=client_cert)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssl_sock:
            ssl_sock.connect((host, port))
            ssl_sock.sendall(msg)
            response = ssl_sock.recv(1024)
    
    return response

# def main():

#     root = tk.Tk()
#     client_var = tk.StringVar(root)
#     client_var.set('Select a client')
#     clinets = {"REST": 'JohnRESTClient',
#                "TCP": 'JohnTCPClient',
#                'UDP': 'JohnUDPServer',
#                'IP': 'JohnIPRange',
#                }
#     client_menu = tk.OptionMenu(root, client_var, *clinets.keys())
#     client_menu.pack()

#     button = tk.Button(root, text="Connect",
#                        command=lambda: execute_client(client_var.get()))
#     button.pack()

#     root.mainloop()


# if __name__ == '__main__':
    # instance = JohnIPRange()
    # instance.ipd4range('123.45.67.64/27')
    # instance.ipd6range("2001:db8::/64")
    # download_folder = 'downloads'
    # if not os.path.exists(download_folder):
    #     os.makedirs(download_folder)
    # main()
    # create an HTTP server and bind it to a port
    # PORT = 8001

    # with socketserver.TCPServer(("", PORT), JohnInterfaceHandler) as httpd:
    #     print(f"Server running on port {PORT}")

    #     # keep the server running until interrupted
    #     try:
    #         httpd.serve_forever()
    #     except KeyboardInterrupt:
    #         pass

    #     httpd.server_close()
    # create a server instance and register the function
    # JohnAuthenticationHandler()
