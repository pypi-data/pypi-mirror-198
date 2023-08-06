import socket
import logging

logger = logging.getLogger("URInterface.TCP")

class TCPClient:
    def __init__(self, ip: str, port: int):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

        logger.debug(f'Created connection to {ip}:{port}')
    
    def send(self, msg: str):
        self.socket.send(msg.encode())
    
    def read(self, size=1024) -> bytes:
        return self.socket.recv(size)

class TCPServer:
    pass