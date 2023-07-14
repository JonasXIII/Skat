import socket
import time
from Skat import *



def main(): 
    print("Welcome to Skat!")

    build_connections()

    global Skat
    Skat = []

    play_round()
    time.sleep(1000)


    

def build_connections():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 8000))
    s.listen()
    print("Waiting for connections...")
    global conn1, addr1, player1
    global conn2, addr2, player2
    global conn3, addr3, player3
    conn1, addr1= s.accept()
    conn2, addr2 = s.accept()
    conn3, addr3 = s.accept()

    player1 = Player(conn1.recv(1024).decode())
    player2 = Player(conn2.recv(1024).decode())
    player3 = Player(conn3.recv(1024).decode())

    print("Name 1 = "+player1.name)
    print("Name 2 = "+player2.name)
    print("Name 3 = "+player3.name)
    



def deal_cards():
    Skat = []
    Skat.append(deal(allCards, player1, player2,player3))
    
    tellAll("deal")

    conn1.sendall(",".join(str(id) for id in [card.id for card in player1.hand]).encode())
    conn2.sendall(",".join(str(id) for id in [card.id for card in player2.hand]).encode())
    conn3.sendall(",".join(str(id) for id in [card.id for card in player3.hand]).encode())


    print("Hands sent")
    for card in Skat:
        print(card)

def play_round():
    for i in range(3):
        deal_cards()
        bid()
        play()
        report_hand_results()
def bid():
    pass
def play():
    pass
def report_hand_results():
    pass


def connected(conn, addr):
    print(f"Player connected from {addr}")
    name = conn.recv(1024).decode()
    msg = name + ", you have succesfully conneted to server."
    conn.sendall(msg.encode())
    return name

def tellAll(msg):
    conn1.sendall(msg.encode())
    conn2.sendall(msg.encode())
    conn3.sendall(msg.encode())
    print(msg)


if __name__ == "__main__":
    main()