import socket
import time
from Skat import *
from cardDealer import *

players = []
trump_suit = 'n'

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
    conn1, addr1= s.accept()
    conn2, addr2 = s.accept()
    conn3, addr3 = s.accept()

    players.append(Player(conn1.recv(1024).decode(), conn1, addr1))
    players.append (Player(conn2.recv(1024).decode(), conn2, addr2))
    players.append(Player(conn3.recv(1024).decode(), conn3, addr3))
    players.sort(key=lambda player: player.name)

    print("Name 1 = "+players[0].name)
    print("Name 2 = "+players[1].name)
    print("Name 3 = "+players[2].name)
    



def deal_cards():
    Skat = []
    Skat.append(deal(ALL_CARDS, players[0], players[1],players[2], 11))
    
    tellAll("deal")
    send_msg(",".join(str(id) for id in [card.id for card in players[0].hand]), players[0])
    send_msg(",".join(str(id) for id in [card.id for card in players[1].hand]), players[1])
    send_msg(",".join(str(id) for id in [card.id for card in players[2].hand]), players[2])


    print("Hands sent")
    for card in Skat:
        print(card)

def play_round():
    for i in range(1):
        deal_cards()
        winning_bid, solo_playuer = bid()
        play(solo_playuer)
        report_hand_results()
def bid():
    global highest_bid
    highest_bid, solo_player = bidding(players[0], players[1], players[2])
    return highest_bid, solo_player

def play(solo_player):
    tellAll("play_hand")
    solo_player_pos = 0
    leadPlayer = solo_player_pos
    for i in range(10):
        leadPlayer = play_trick(leadPlayer)


def tell_A_B_played_card(A, B, card):
    send_msg("info", A)
    send_msg(B.name, A)
    send_msg(card.name, A)

def getWinner(card1, card2, card3, trump):
    print(f"cards are {card1.name}, {card2.name}, {card3.name}")
    card1Value = card1.id
    card2Value = card2.id
    card3Value = card3.id
    if card1.suit == trump or card1.rank == "U":
        card1Value += 80
    elif card1.suit == card1.suit:
        card1Value += 40
    if card2.suit == trump or card2.rank == "U":
        card2Value += 80
    elif card2.suit == card1.suit:
        card2Value += 40
    if card3.suit == trump or card3.rank == "U":
        card3Value += 80
    elif card3.suit == card1.suit:
        card3Value += 40
    if max(card1Value, card2Value, card3Value) == card1Value:
        print("card1 wins")
        return 0
    elif max(card1Value, card2Value, card3Value) == card2Value:
        print("card2 wins")
        return 1
    else:
        print("card3 wins")
        return 2



def play_trick(StartPlayer):
    send_msg("play_card", players[StartPlayer])
    cardplayed1 = players[StartPlayer].hand.pop(int(recv(players[StartPlayer])))
    tell_A_B_played_card(players[(StartPlayer+1)%3], players[(StartPlayer)%3], cardplayed1)
    tell_A_B_played_card(players[(StartPlayer+2)%3], players[(StartPlayer)%3], cardplayed1)
    
    send_msg("play_card", players[(StartPlayer+1)%3])
    cardplayed2 = players[(StartPlayer+1)%3].hand.pop(int(recv(players[(StartPlayer+1)%3])))
    tell_A_B_played_card(players[(StartPlayer+2)%3], players[(StartPlayer+1)%3], cardplayed2)
    tell_A_B_played_card(players[(StartPlayer)%3], players[(StartPlayer+1)%3], cardplayed2)

    send_msg("play_card", players[(StartPlayer+2)%3])
    cardplayed3 = players[(StartPlayer+2)%3].hand.pop(int(recv(players[(StartPlayer+2)%3])))
    tell_A_B_played_card(players[(StartPlayer+1)%3], players[(StartPlayer+2)%3], cardplayed3)
    tell_A_B_played_card(players[(StartPlayer)%3], players[(StartPlayer+2)%3], cardplayed3)

    trickwinner = getWinner(cardplayed1, cardplayed2, cardplayed3, trump_suit)
    tellAll("trick_winner")
    tellAll(players[(trickwinner+StartPlayer) %3].name)
    return (trickwinner+StartPlayer)%3



def report_hand_results():
    pass



def tellAll(msg):
    send_msg(msg, players[0])
    send_msg(msg, players[1])
    send_msg(msg, players[2])



def send_msg(msg, player):
    message_length = len(msg)
    player.conn.sendall(message_length.to_bytes(4, byteorder='big') + msg.encode())

def recv(player):
    message_length = int.from_bytes(player.conn.recv(4), byteorder='big')
    return player.conn.recv(message_length).decode()

def getBiddingOkay(player, bid):
    print (f"asking {player.name} if they want to bid {bid}")
    send_msg("bid", player)
    send_msg(str(bid), player)
    return recv(player) == "okay"

def bidding_winner(player, bid):
    tellAll("winning_bid")
    tellAll(player.name)
    tellAll(str(bid))

def bidding_info(player, bid):
    tellAll("info")
    tellAll(player.name)
    tellAll(str(bid))

def bidding(pos1, pos2, pos3):
    tellAll("bidding")
    print("anounced bidding")
    in1 = True
    in2 = True
    in3 = True
    bid = -1
    while True:
        bid+=1
        #ask pos2 and pos 1 if they will bid next bid
        if getBiddingOkay(pos2, BIDDING_ORDER[bid]):
            bidding_info(pos2, BIDDING_ORDER[bid])
            if not getBiddingOkay(pos1, BIDDING_ORDER[bid]):
                bidding_info(pos1, 0)
                while True:
                    bid+=1
                    #ask pos3 and pos2 after pos1 is out
                    if getBiddingOkay(pos3, BIDDING_ORDER[bid]):
                        bidding_info(pos3, BIDDING_ORDER[bid])
                        if not getBiddingOkay(pos2, BIDDING_ORDER[bid]):
                            bidding_info(pos2, 0)
                            bidding_winner(pos3, BIDDING_ORDER[bid])
                            return bid,pos3
                        else:
                            bidding_info(pos2, BIDDING_ORDER[bid])
                    else:
                        bidding_info(pos3, 0)
                        bidding_winner(pos2, BIDDING_ORDER[bid-1])
                        return bid-1,pos2
            else:
                bidding_info(pos1, BIDDING_ORDER[bid])
        else:
            bidding_info(pos2, 0)
            bid-=1
            while True:
                bid+=1
                #ask pos3 and pos1 after pos2 is out
                if getBiddingOkay(pos3, BIDDING_ORDER[bid]):
                    bidding_info(pos3, BIDDING_ORDER[bid])
                    if not getBiddingOkay(pos1, BIDDING_ORDER[bid]):
                        bidding_info(pos1, 0)
                        bidding_winner(pos3, BIDDING_ORDER[bid])
                        return bid,pos3
                    else:
                        bidding_info(pos1, BIDDING_ORDER[bid])
                else:
                    bidding_info(pos3, 0)
                    if bid==0:
                        if getBiddingOkay(pos1, BIDDING_ORDER[bid]):
                            bidding_info(pos1, BIDDING_ORDER[bid])
                            bidding_winner(pos1, BIDDING_ORDER[bid])
                            return bid,pos1
                        else:
                            bidding_winner("no one", 0)
                            return bid-1, pos1
                    else:
                        bidding_winner(pos1, BIDDING_ORDER[bid-1])
                        return bid-1,pos1
                    


if __name__ == "__main__":
    main()