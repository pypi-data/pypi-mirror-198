import ssl
import socket
import threading
# Defining a class to act as an SSL server
class SSLServer:
    def __init__(self, host, port, certfile, keyfile):
        """
        Constructor method for SSLServer.

        Args:
            host (str): The hostname or IP address the server should bind to.
            port (int): The port number the server should listen on.
            certfile (str): The path to the SSL certificate file.
            keyfile (str): The path to the SSL key file.
        """
        self.host = host
        self.port = port
        self.certfile = certfile
        self.keyfile = keyfile

    def start(self):
        """
        Start the SSL server.
        """
        # Creating an SSL context with CLIENT_AUTH purpose
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        
        # Loading the SSL certificate and key
        context.load_cert_chain(certfile=self.certfile, keyfile=self.keyfile)

        # Creating a socket with IPv4 and TCP protocol
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Binding the server to the specified host and port
            server_socket.bind((self.host, self.port))
            # Starting to listen for incoming connections
            server_socket.listen(1)

            # Waiting for incoming connections
            while True:
                conn, addr = server_socket.accept()
                # Wrapping the socket with SSL
                conn_ssl = context.wrap_socket(conn, server_side=True)

                # Do something with conn_ssl
                data = conn_ssl.recv(1024)
                conn_ssl.sendall(b"Hello, client!")
                conn_ssl.close()


# Defining a class to act as an SSL client
class SSLClient:
    def __init__(self, host, port, certfile):
        """
        Constructor method for SSLClient.

        Args:
            host (str): The hostname or IP address of the SSL server.
            port (int): The port number the SSL server is listening on.
            certfile (str): The path to the SSL certificate file of the SSL server.
        """
        self.host = host
        self.port = port
        self.certfile = certfile

    def connect(self):
        """
        Connect to the SSL server.
        """
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_verify_locations(cafile=self.certfile)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn_ssl = context.wrap_socket(client_socket, server_hostname=self.host)
        self.conn_ssl.connect((self.host, self.port))

    def sendall(self, data):
        self.conn_ssl.sendall(data)

    def recv(self, bufsize):
        return self.conn_ssl.recv(bufsize)

    def close(self):
        self.conn_ssl.close()
