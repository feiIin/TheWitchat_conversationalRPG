from struct import pack

STRING_UTF8 = bytearray([0xAC, 0x08, 0x81, 0x16])
INT32 = bytearray([0x81, 0x32])
HEAD = bytearray([0xDE, 0xAD])
TAIL = bytearray([0xBE, 0xEF])
REMOTE = b'Remote'

class TCPrequest:

    def __init__(self):
        self.payload = bytearray()
    
    def utf8(self, token):
        return self.append(STRING_UTF8) \
            .len_short(len(token)) \
            .append(token)
    def int32(self, value):
        iv = value
        if(iv & 0x80000000):
            iv = -0x100000000 + iv
        return self.append(INT32) \
            .append(pack("!l", iv))
    
    def len_short(self, length):
        return self.append(pack("!H", length))

    def append(self, data):
        self.payload.extend(data)
        return self

    def end(self):
        self.append(TAIL)
        self.payload = bytearray(HEAD) + pack("!H", len(self.payload) + 4) + self.payload
        return self.payload