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


class TestJohnServer(unittest.TestCase):

    def setUp(self):
        self.rest_server = JSA.JohnRESTServer()

    def test_rest_get_data(self):
        print('test rest_get_data')

        data = self.rest_server.get_data("objects", "1")
        data = json.loads(data)
        self.assertIsInstance(data, dict)

    # ... more test methods for other methods in the class ...
    def test_rest_post_data(self):
        print('test rest_post_data')

        data = {
            "title": "Test title",
            "body": "Test body",
            "id": 1,
        }
        response = self.rest_server.post_data(
            endpoint='objects', param=1, data=data)
        self.assertIsInstance(response, dict)

        # Add assertions based on the expected response

    def test_rest_put_data(self):
        print('test rest_put_data')

        response = self.rest_server.put_data(endpoint='objects', param=1)
        self.assertIsInstance(response, dict)

        # Add assertions based on the expected response

    def test_rest_delete_data(self):
        print('test rest_delete_data')

        response = self.rest_server.delete_data(endpoint='objects', param=1)
        self.assertEqual(response, 200)
        # Add assertions based on the expected response

    def test_ipd4range(self):
        print('test ip4')

        ip_range = JSA.JohnIPRange()
        cidr = "192.168.1.0/30"
        expected_ips = [ipaddress.IPv4Address('192.168.1.0'), ipaddress.IPv4Address(
            '192.168.1.1'), ipaddress.IPv4Address('192.168.1.2'), ipaddress.IPv4Address('192.168.1.3')]
        self.assertEqual(ip_range.ipd4range(cidr), expected_ips)

    # testing JohnInterfaceHandler
    def test_client_server_interaction(self):
        print('test client_server_interaction')

        server_address = ('localhost', 8001)
        with HTTPServer(server_address, JSA.JohnInterfaceHandler) as httpd:
            # Start the server in a separate thread
            server_thread = threading.Thread(target=httpd.serve_forever)
            server_thread.start()

            conn = http.client.HTTPConnection("localhost", 8001)
            conn.request("GET", "/?command=status")
            response = conn.getresponse()

            data = json.loads(response.read().decode())
            print('data: ', data)
            self.assertEqual(data, {"status": "ok"})

            conn.request("GET", "/?command=stop")
            response = conn.getresponse()
            data = json.loads(response.read().decode())
            print('data: ', data)

            self.assertEqual(data, {"status": "stopped"})

            conn.request("GET", "/?command=unknown")
            response = conn.getresponse()
            data = json.loads(response.read().decode())
            print('data: ', data)

            self.assertEqual(
                data, {"status": "error", "message": "Unknown command"})

            conn.close()

            # Shutdown the server and close the socket
            httpd.shutdown()
            httpd.server_close()
            server_thread.join()

    @staticmethod
    def run_server():
        HOST, PORT = "localhost", 9999
        with socketserver.TCPServer((HOST, PORT), JSA.JohnTCPServer) as server:
            server.timeout = 2  # Timeout after 2 seconds
            server.handle_request()

    def test_ssl_authenticate(self):
        """
        using the multiprocessing module to start the server in a separate process during the test"""
        import time
        print('test ssl authenticate')
        certfile='server.crt'
        keyfile='server.key'
        HOST='localhost'
        PORT=12346
        server_process = multiprocessing.Process(
            target=JSA.JohnAuthenticationHandler, args=(certfile, keyfile, HOST, PORT))
        server_process.start()
        # Give the server some time to start accepting connections
        time.sleep(1)

        input_data = b"Hello, server!"
        client_cert='ca.crt'
        host='localhost'
        port=12346
        response = JSA.ssl_client(input_data, client_cert, host, port)
        expected_output = b"Hello, client!"
        self.assertEqual(response, expected_output)

        server_process.terminate()
        server_process.join()

    def test_JohnXMLRPCRequestHandler(self):
        print('test xmlrpc request handler')

        handler = JSA.JohnXMLRPCRequestHandler()
        self.assertEqual(handler.add(5, 3), 8)


if __name__ == '__main__':
    unittest.main()
