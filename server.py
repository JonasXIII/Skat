import socket



def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 8000))
    s.listen()
    print("Waiting for connections...")
    conn1, addr1 = s.accept()
    print(f"Player 1 connected from {addr1}")
    conn1.sendall(b"Connected to server")
    conn2, addr2 = s.accept()
    print(f"Player 2 connected from {addr2}")
    conn2.sendall(b"Connected to server")
    conn3, addr3 = s.accept()
    print(f"Player 3 connected from {addr3}")
    conn3.sendall(b"Connected to server")
    while True:
        n=1


if __name__ == "__main__":
    main()