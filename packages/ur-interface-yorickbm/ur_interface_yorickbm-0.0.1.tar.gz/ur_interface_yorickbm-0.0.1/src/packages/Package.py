import struct

class Package:
    def __init__(self):
        self.index = 0
        self.data = bytes()
    
    def parse(self) -> None:
        pass
    
    def setData(self, data: bytes):
        self.index = 0
        self.data = data

    def popInt64(self) -> int:
        return int(self._pop("!Q", 8))

    def popInt32(self) -> int:
        return int(self._pop("!i", 4))
    
    def popInt16(self) -> int:
        return int(self._pop("!h", 2))
    
    def popUInt8(self) -> int:
        return int(self._pop("!I", 1))
    
    def popFloat(self) -> float:
        return float(self._pop("!f", 4))
    
    def popDouble(self) -> float:
        return float(self._pop("!d", 8))
    
    def popBool(self) -> bool:
        return bool(self._pop("!?", 1))
    
    def popUChar(self) -> int:
        return int(self._pop("!B", 1))

    def _pop(self, type: str, bytesCount: int) -> any:
        data = struct.unpack(type, self.data[self.index:self.index+bytesCount])[0]
        self.index += bytesCount
        return data

class PackageHandler:
    def __init__(self):
        self.packets = [None] * 16

    def registerPacket(self, packet, type: int) -> None:
        self.packets[type] = packet

    def parse(self, data: bytes) -> None:
        length =  (struct.unpack('!i', data[0:4]))[0]
        type = (struct.unpack('!b', data[4:5]))[0]

        if type != 16: # 16 is URe data packet type
            return False
        
        i =0
        while i+5 < length:
            msglen = (struct.unpack('!i', data[5 + i:9 + i]))[0]
            msgtype = (struct.unpack('!B', data[9+ i:10+ i]))[0]
            msgdata = data[10+i:i + msglen]
            i += msglen

            packet:Package = self.packets[msgtype]
            if packet == None:
                continue

            packet.setData(msgdata)
            packet.parse()



    
        