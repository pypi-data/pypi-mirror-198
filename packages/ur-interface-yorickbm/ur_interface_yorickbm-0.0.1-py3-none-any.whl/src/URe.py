import logging
import struct
from threading import Thread

from .packages.RobotModePacket import RobotModePacket
from .packages.Package import PackageHandler
from .TCP import TCPClient

class URe():
    def __init__(self, ip):
        self.handler = PackageHandler()
        self.client = TCPClient("192.168.1.120", 30001)
        self.isAlive = True

        self.thread = Thread(target=self.robotThread, args=())
        self.thread.start()
    
    def robotThread(self):
        while self.isAlive:
            data = self.client.read(4096)
            self.handler.parse(data)

            self.onThreadRun()
            
    def onThreadRun(self):
        pass

    def shutdown(self):
        self.isAlive = False # Kill thread
        self.thread.join() # Wait for it to be finished

