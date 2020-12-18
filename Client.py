import socket

DIS_MSG = "disconnect"
FORMAT = "utf-8"
HEADER = 64
PORT = 9090
SERVER = "192.168.1.8"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
def start():
    connetced = True
    while connected:
        vaule = str(input())
        send(vaule)
        if vaule == "disconenct":
            break
start()