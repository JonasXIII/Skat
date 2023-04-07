import socket

name = ""

def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("localhost", 8000))
    
    connected(conn)
    recv(conn)
    recv(conn)




def bidding():
    pass

def connected(conn):
    name = conn.recv(1024).decode()
    print(f"Connection to server succesful, you are {name}.")

def recv(conn):
    data = conn.recv(1024).decode()
    print(data)


if __name__ == "__main__":
    main()