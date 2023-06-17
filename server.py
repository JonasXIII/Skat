import socket
import time
from Skat import *




def main(): 

    build_connections()
    
    play_round()
    time.sleep(1000)


    

def build_connections():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 8000))
    s.listen()
    print("Waiting for connections...")
    global conn1, addr1, name1
    global conn2, addr2, name2
    global conn3, addr3, name3
    conn1, addr1= s.accept()
    name1 = connected(conn1,addr1)
    conn2, addr2 = s.accept()
    name2 = connected(conn2,addr2)
    conn3, addr3 = s.accept()
    name3 = connected(conn3,addr3)
    
    tellAll(conn1,conn2,conn3,"Three people have successfully connected. Here we go!")

def deal_cards():
    deal(allCards, player1, player2,player3)
    
    sendHand(conn1, player1)
    sendHand(conn2, player2)
    sendHand(conn3, player3)

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

def sendHand(conn, player):
    msg = player.name+" your hand is "+ player.getHand()
    print(f"Sending: {msg}")
    conn.sendall(msg.encode())


def connected(conn, addr):
    print(f"Player connected from {addr}")
    name = conn.recv(1024).decode()
    msg = name + ", you have succesfully conneted to server."
    conn.sendall(msg.encode())
    return name

def tellAll(conn1,conn2,conn3,msg):
    conn1.sendall(msg.encode())
    conn2.sendall(msg.encode())
    conn3.sendall(msg.encode())
    print(msg)


if __name__ == "__main__":
    main()