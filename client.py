import socket
import time
from Skat import *

print("Welcome to Skat!")

def main():
       
    get_connected()
    while True:
        next_thing = recv()

        if next_thing == "deal":
            recieve_hand()
        elif next_thing == "bidding":
            bidding()
        elif next_thing == "play_hand":
            play_hand()
        
def send_msg(msg):
    message_length = len(msg)
    player.conn.sendall(message_length.to_bytes(4, byteorder='big') + msg.encode())

def recv():
    message_length = int.from_bytes(player.conn.recv(4), byteorder='big')
    return player.conn.recv(message_length).decode()

def play_hand():
    print("Playing hand.")
    while True:
        next = recv()
        if next == "play_card":
            print_hand_with_ids()
            card = input("PLay a card:")
            print(f"{player.hand.pop(int(card))}.")
            send_msg(card)
        elif next == "info":
            player_name = recv()
            card = recv()
            print(f"{player_name} played {card}.")
        elif next == "trick_winner":
            trick_winner = recv()
            print(f"{trick_winner} won the trick.")
        elif next == "trump":
            trump = recv()
            print(f"The trump suit is {trump}.")
        elif next == "hand_winner":
            winner = recv()
            print(f"{winner} won the hand.")
            return


def print_hand_with_ids():
     # Print the header row with numbers
    for i in range(len(player.hand)):
        print(f"{i}", end="|")
    print()  # Newline after header row
    
    # Print the characters row with pipe separators
    for card in player.hand:
        print(f"{card}", end="|")
    print()  # Newline after characters row

def recieve_hand():
    ids = recv()
    player.hand = [get_card(id) for id in ids.split(",")]
    player.printHand()

def bidding():
    print("Bidding started.")
    while True:
        next = recv()
        if next == "bid":
            bid = int(recv())
            while True: 
                okay = input(f"{player.name}, do you want to bid {bid}? (y/n) ")
                print()
                if okay == "y" or okay == "y ":
                    send_msg("okay")
                    break
                elif okay == "n" or okay == "n ":
                    send_msg("no")
                    break
                else:
                    print("Invalid input.") 
    

        elif next == "info":
            player_name = recv()
            bid = int(recv())
            if player_name != player.name:
                if bid > 0:
                    print(f"{player_name} bid {bid}.")
                else:
                    print(f"{player_name} passed.")
        elif next == "winning_bid":
            winning_bid = recv()
            winning_bid_player = recv()
            print(f"The winning bid is {winning_bid} by {winning_bid_player}.")
            return

def get_connected():
    global player
    
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("localhost", 8000))
    name = input("What would you like to be called? ")
    if name[-1] == " ":
        name = name[:-1]
    player = Player(name, conn, 0)
    print()
    send_msg(name)




if __name__ == "__main__":
    main()
