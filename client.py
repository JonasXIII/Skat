import socket



def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8000))
    data = s.recv(1024).decode()
    print(data)
    s.sendall()

    while True:
        n=1

if __name__ == "__main__":
    main()