import socket
import threading 
import beepy

DIS_MSG = "disconnect"
FORMAT = "utf-8"
HEADER = 64
PORT = 9090
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
print(SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[Server]: New Connection - {addr} connected") 

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DIS_MSG:
                connected = False
        
            if msg == "ping":
                print(f"[Server]: Address = {addr} Message = {msg}")
                beepy.beep(sound=4)
            else:
                print(f"[Server]: Address = {addr} Message = {msg}")
                beepy.beep(sound=1)


    
    conn.close()

def start():
    server.listen()
    print(f"[Server]: Listening... {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Server]: Active connections - {threading.activeCount() - 1} ")
    


print("[Server]: Starting... ")
start()



 
  
