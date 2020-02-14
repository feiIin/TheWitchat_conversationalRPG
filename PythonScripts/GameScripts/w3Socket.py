import socket
from TCPrequest import TCPrequest, REMOTE

HOST, PORT = '127.0.0.1', 37001


class W3socket:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        self.sock.connect((HOST,PORT))

    def close(self):
        self.sock.close()

    def execute_cmd(self, cmd):
        self.sock.send(TCPrequest()
            .utf8(REMOTE)
            .int32(0x12345678)
            .int32(0x81160008)
            .utf8(cmd.encode('utf-8'))
            .end())

#USED FOR TESTING
if __name__ == '__main__':
    mySocket = W3socket()
    mySocket.connect()
    mySocket.execute_cmd("printString")
    mySocket.close()