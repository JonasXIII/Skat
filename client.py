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
            msg = "What card would you like to play? \n"
            for i in player.hand:
                msg.join(f"{i}: {player.hand[i]} \n")
            card = input(msg)
            send_msg(card)
        elif next == "info":
            player_name = recv()
            card = recv()
            print(f"{player_name} played {card}.")
        elif next == "winning_card":
            winning_card = recv()
            winning_card_player = recv()
            print(f"The winning card is {winning_card} by {winning_card_player}.")
        elif next == "trick_winner":
            trick_winner = recv()
            print(f"{trick_winner} won the trick.")
        elif next == "hand_winner":
            hand_winner = recv()
            print(f"{hand_winner} won the hand.")
            return
        elif next == "trick":
            trick = recv()
            print(f"Trick {trick}:")
        elif next == "trick_info":
            player_name = recv()
            card = recv()
            print(f"{player_name} played {card}.")
        elif next == "hand_info":
            player_name = recv()
            card = recv()
            print(f"{player_name} has {card} cards left.")
        elif next == "hand":
            hand = recv()
            print(f"Your hand is {hand}.")
        elif next == "trump":
            trump = recv()
            print(f"The trump suit is {trump}.")
        elif next == "hand_trump":
            hand_trump = recv()
            print(f"Your hand and the trump suit is {hand_trump}.")
        elif next == "hand_trick":
            hand_trick = recv()
            print(f"Your hand and the trick is {hand_trick}.")
        elif next == "hand_trump_trick":
            hand_trump_trick = recv()
            print(f"Your hand, the trump suit, and the trick is {hand_trump_trick}.")
        elif next == "hand_trump_trick_winner":
            hand_trump_trick_winner = recv()
            print(f"Your hand, the trump suit, the trick, and the winning card is {hand_trump_trick_winner}.")
        elif next == "hand_trump_trick_winner_info":
            player_name = recv()
            card = recv()
            print(f"{player_name} played {card}.")


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
    player = Player(input("What would you like to be called? "), conn, 0)
    name = player.name
    print()
    send_msg(name)




if __name__ == "__main__":
    main()
