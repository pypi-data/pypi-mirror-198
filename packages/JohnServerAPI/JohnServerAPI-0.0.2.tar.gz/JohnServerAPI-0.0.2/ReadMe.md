# Title: John's Custom HTTP Client/Server Library

Description: This library provides a custom implementation of various network services and protocols such as REST, TCP, UDP, IP range calculation, and SSL/TLS. It offers the ability to interact with RESTful APIs, send/receive data over TCP or UDP, manage IP ranges, and secure data using SSL/TLS.

## Classes and Functions

JohnRESTServer
A class for interacting with RESTful APIs.

```
__init__(self): Initializes the class and sets the base URL for the RESTful API.
get_data(self, endpoint='objects', param=1): Sends a GET request to the specified endpoint and returns the data.
post_data(self, endpoint='objects', param=1, data={...}): Sends a POST request to the specified endpoint with the given data.
put_data(self, endpoint='objects', param=1): Sends a PUT request to the specified endpoint with the given data.
delete_data(self, endpoint='objects', param=1): Sends a DELETE request to the specified endpoint.
```

## JohnTCPServer
A class for handling TCP connections.

handle(self): Processes incoming data from the client and sends a response back.
JohnUDPServer
A class for handling UDP connections.

handle(self): Processes incoming data from the client and sends a response back.
JohnIPRange
A class for managing IP ranges.

ipd4range(self, cidr): Calculates and returns a list of IPv4 addresses within the given CIDR range.
ipd6range(self, cidr): Calculates and returns a list of IPv6 addresses within the given CIDR range.
process_command(command)
A function that processes incoming commands and returns a response.

JohnInterfaceHandler
A class for handling HTTP requests.

do_GET(self): Processes incoming GET requests and sends a response back.
JohnXMLRPCReqHandler
A class that inherits from SimpleXMLRPCRequestHandler.

JohnXMLRPCRequestHandler
A class for handling XML-RPC requests.

__init__(self, url='localhost', port=8000): Initializes the class and sets up the XML-RPC server.
start_server(self): Starts the XML-RPC server.
add(self, x, y): A sample XML-RPC function that adds two numbers and returns the result.
JohnAuthenticationHandler
A function for handling SSL/TLS connections. It accepts incoming connections and receives data.

ssl_client(msg, client_cert='ca.crt', host='localhost', port=12345)
A function that sends a message to an SSL/TLS server and receives a response.

Example Usage

```
from JohnServerAPI import JohnRESTServer, JohnTCPServer, JohnUDPServer, JohnIPRange, JohnInterfaceHandler, JohnXMLRPCRequestHandler, JohnAuthenticationHandler, ssl_client

# Interact with a RESTful API
rest_server = JohnRESTServer()
data = rest_server.get_data()

# Create and run a TCP server
tcp_server = socketserver.TCPServer(("", PORT), JohnTCPServer)
tcp_server.serve_forever()

# Create and run a UDP server
udp_server = socketserver.UDPServer(("", PORT), JohnUDPServer)
udp_server.serve_forever()

# Calculate IP ranges
ip_range = JohnIPRange()
ipv4_range = ip_range.ipd4range('123.45.67.64/27')
ipv6_range = ip_range.ipd6range('2001:db8::/64')

# Create and run an HTTP server
http_server = socketserver.TCPS
```

TestJohnServer
This is a test suite for the JohnServerAPI module. It contains multiple test cases to ensure that the different functionalities of the JohnServerAPI are working correctly.

Importing Dependencies
```
import unittest
import sys
sys.path.append('../1st')
import JohnServerAPI.JohnServerAPI as JSA

import threading
import socketserver
from http.server import HTTPServer
import json
import http.client

import multiprocessing
import ipaddress
```

# Test Class
The TestJohnServer class inherits from unittest.TestCase and contains several test methods for different functionalities provided by the JohnServerAPI.

```
class TestJohnServer(unittest.TestCase):
```

## setUp
The setUp method initializes the test environment and is executed before each test case.

```
def setUp(self):
    self.rest_server = JSA.JohnRESTServer()
```

## test_rest_get_data
This test case checks if the get_data method of JohnRESTServer returns the expected data.

```
def test_rest_get_data(self):
```

## test_rest_post_data
This test case checks if the post_data method of JohnRESTServer returns the expected response.

```
def test_rest_post_data(self):
```

## test_rest_put_data
This test case checks if the put_data method of JohnRESTServer returns the expected response.

```
def test_rest_put_data(self):
```

## test_rest_delete_data
This test case checks if the delete_data method of JohnRESTServer returns the expected response.

```
def test_rest_delete_data(self):
```

## test_ipd4range
This test case checks if the ipd4range method of JohnIPRange returns the expected IP range.

```
def test_ipd4range(self):
```

## test_client_server_interaction
This test case checks if the client-server interaction using JohnInterfaceHandler works correctly.

```
def test_client_server_interaction(self):
```

## run_server
This static method starts a TCP server using JohnTCPServer.

```
@staticmethod
def run_server():
```

## test_ssl_authenticate
This test case checks if the SSL authentication using JohnAuthenticationHandler works correctly.


def test_ssl_authenticate(self):

## test_JohnXMLRPCRequestHandler
This test case checks if the JohnXMLRPCRequestHandler processes requests correctly.


```
def test_JohnXMLRPCRequestHandler(self):
```

## Running the Test Suite
The test suite is run using the unittest.main() function.

```
if __name__ == '__main__':
    unittest.main()
```

This test suite helps ensure the correct functionality of the JohnServerAPI module by covering different aspects of the code.



# Socket and SSL 
## Create crt and key files for server and client
Here are the steps to create a self-signed SSL/TLS certificate and private key for a server:

Generate a private key for the server:


```
openssl genrsa -out server.key 2048
```
Generate a certificate signing request (CSR) for the server:

```
openssl req -new -key server.key -out server.csr
```
Generate a self-signed SSL/TLS certificate for the server:

```
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```

Here are the steps to create a self-signed SSL/TLS certificate and private key for a client:
Generate a private key for the client:

```
openssl genrsa -out client.key 2048
```
Generate a certificate signing request (CSR) for the client:

```
openssl req -new -key client.key -out client.csr
```
Generate a self-signed SSL/TLS certificate for the client:

```
openssl x509 -req -days 365 -in client.csr -signkey client.key -out client.crt```


## share certificate files between the server and client
Sure, here are the codes for each step:

Create a new file called chain.pem and open it in a text editor:
```
with open('chain.pem', 'w') as f:
    pass
    ```
Copy the contents of the client's SSL/TLS certificate (client.crt) into the chain.pem file:
```
with open('client.crt', 'r') as client_cert_file, open('chain.pem', 'a') as chain_file:
    client_cert_contents = client_cert_file.read()
    chain_file.write(client_cert_contents)
```
Copy the contents of the server's SSL/TLS certificate (server.crt) into the chain.pem file, below the client's certificate:
```
with open('server.crt', 'r') as server_cert_file, open('chain.pem', 'a') as chain_file:
    server_cert_contents = server_cert_file.read()
    chain_file.write(server_cert_contents)
```
Save and close the chain.pem file:


Note that you can combine steps 2 and 3 into a single block of code, like this:

```
with open('client.crt', 'r') as client_cert_file, open('server.crt', 'r') as server_cert_file, open('chain.pem', 'w') as chain_file:
    client_cert_contents = client_cert_file.read()
    server_cert_contents = server_cert_file.read()
    chain_file.write(client_cert_contents + server_cert_contents)
```
This code block opens both the client.crt and server.crt files, reads their contents, and writes them to the chain.pem file.

## codes for server and client

For Server: 

```
import ssl

# Create an SSL context and load the server's certificate and private key
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile='server.crt', keyfile='server.key')

# Load the certificate chain file
ssl_context.load_verify_locations(cafile='chain.pem')
```
For Client
```
import ssl

# Create an SSL context and load the client's certificate and private key
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_cert_chain(certfile='client.crt', keyfile='client.key')

# Load the CA file as a trusted root CA
ssl_context.load_verify_locations(cafile='ca.crt')

# Create a socket and connect to the server
ssl_sock = ssl_context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
ssl_sock.connect((HOST, PORT))

# Perform the SSL/TLS handshake and send data
ssl_sock.sendall(b'Hello, server!')
data = ssl_sock.recv(1024)

# Close the SSL/TLS connection
ssl_sock.close()
```
