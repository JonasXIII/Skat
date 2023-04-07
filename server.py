import socket
from Skat import *


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 8000))
    s.listen()
    print("Waiting for connections...")
    conn1, addr1 = s.accept()
    connected(conn1,addr1, "Silke")
    conn2, addr2 = s.accept()
    connected(conn2,addr2, "Jork")
    conn3, addr3 = s.accept()
    connected(conn3,addr3, "Jonas")
    
    tellAll(conn1,conn2,conn3,"Wellcome to Skat, three people have successfully connected.")
    deal(allCards, player1, player2,player3)
    
    sendHand(conn1, player1)
    sendHand(conn2, player2)
    sendHand(conn3, player3)




def sendHand(conn, player):
    msg = player.name+" your hand is "+ player.getHand()
    print(f"Sending: {msg}")
    conn.sendall(msg.encode())


def connected(conn, addr, name):
    print(f"Player connected from {addr}")
    msg = name #+ ", you have succesfully conneted to server."
    conn.sendall(msg.encode())
    #conn.sendall(b"Connected to server, you are ")

def tellAll(conn1,conn2,conn3,msg):
    conn1.sendall(msg.encode())
    conn2.sendall(msg.encode())
    conn3.sendall(msg.encode())


if __name__ == "__main__":
    main()