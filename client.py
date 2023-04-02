import socket



def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("localhost", 8000))
    
    recv(conn)
    recv(conn)
    recv(conn)




def recv(conn):
    data = conn.recv(1024).decode()
    print(data)


if __name__ == "__main__":
    main()