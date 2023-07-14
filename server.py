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
    global player1
    global player2
    global player3
    conn1, addr1= s.accept()
    conn2, addr2 = s.accept()
    conn3, addr3 = s.accept()

    player1 = Player(conn1.recv(1024).decode(), conn1, addr1)
    player2 = Player(conn2.recv(1024).decode(), conn1, addr2)
    player3 = Player(conn3.recv(1024).decode(), conn1, addr3)

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
    for i in range(1):
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
    player1.conn.sendall(msg.encode())
    player2.conn.sendall(msg.encode())
    player3.conn.sendall(msg.encode())
    print(msg)

def getBiddingOkay(player, bid):
    player.sendall("bid".encode())
    player.sendall(bid.encode())
    return player.recv(1024).decode() == "okay"


def bidding(pos1, pos2, pos3):
    in1 = True
    in2 = True
    in3 = True
    bid = -1
    while True:
        bid+=1
        #ask pos2 and pos 1 if they will bid next bid
        if getBiddingOkay(pos2, biddingOrder[bid]):
            if not getBiddingOkay(pos1, biddingOrder[bid]):
                while True:
                    bid+=1
                    #ask pos3 and pos2 after pos1 is out
                    if getBiddingOkay(pos3, biddingOrder[bid]):
                        if not getBiddingOkay(pos2, biddingOrder[bid]):
                            return bid,pos3
                    else:
                        return bid-1,pos2
        else:
            bid-=1
            while True:
                bid+=1
                #ask pos3 and pos1 after pos2 is out
                if getBiddingOkay(pos3, biddingOrder[bid]):
                    if not getBiddingOkay(pos1, biddingOrder[bid]):
                        return bid,pos3
                else:
                    if bid==0:
                        if getBiddingOkay(pos1, biddingOrder[bid]):
                            return
                    return bid-1, pos1


if __name__ == "__main__":
    main()