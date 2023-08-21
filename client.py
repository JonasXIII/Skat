import socket
import time
from Skat import *
from cardDealer import *

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
        elif next_thing == "solo_player":
            plan_game()

def plan_game():
    print("Planning game.")
    next = recv()
    while True:
        if next == "hand?":
            while True:
                choice = input("Would you like to look at the Skat? (y/n) ")
                if choice == "y" or choice == "y ":
                    send_msg("okay")
                    break
                elif choice == "n" or choice == "n ":
                    send_msg("no")
                    break
        elif next == "skat":
            player.hand.append(get_card(int(recv())))
            player.hand.append(get_card(int(recv())))
            player.hand.sort(key=comp)
            send_msg(str(player.hand.pop(choose_card_from_hand("Choose a card to put back into the Skat.")).id))
            send_msg(str(player.hand.pop(choose_card_from_hand("Choose another card to put back into the Skat.")).id))
        elif next == "trump":
            while True:
                choice = input("Would would you like trump to be? \n(yellow/y)\n(red/r)\n(green/g)\n(blue/b)\n(grand/gd)\n(null/n)\n")
                if choice == "y" or choice == "yellow" or choice == "y " or choice == "yellow ":
                    send_msg("yellow")
                    break
                elif choice == "r" or choice == "red" or choice == "r " or choice == "red ":
                    send_msg("red")
                    break
                elif choice == "g" or choice == "green" or choice == "g " or choice == "green ":
                    send_msg("green")
                    break
                elif choice == "b" or choice == "blue" or choice == "b " or choice == "blue ": 
                    send_msg("blue")
                    break
                elif choice == "gd" or choice == "grand" or choice == "gd " or choice == "grand ":
                    send_msg("grand")
                    break
                elif choice == "n" or choice == "null" or choice == "n " or choice == "null ":
                    send_msg("null")
                    break
            
def choose_card_from_hand(prompt):
    while True:
        print_hand_with_ids()
        choice = input(prompt)
        try:
            choice = int(choice)
            if choice < 0 or choice >= len(player.hand):
                print("Please enter a valid number.")
            else:
                return choice
        except ValueError:
            print("Please enter a valid number.")

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
            card = choose_card_from_hand("Play a card:")
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
