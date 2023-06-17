import socket
import time

name = ""

def main():
    
    
    get_connected()
    recv()
    recv()
    time.sleep(1000)




def bidding():
    pass

def get_connected():
    global conn
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("localhost", 8000))
    name = input("What would you like to be called?")[:-1]
    print()
    conn.sendall(name.encode())

def recv():
    data = conn.recv(1024).decode()
    print(data)


if __name__ == "__main__":
    main()