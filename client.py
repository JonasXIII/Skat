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
        
def send_msg(msg):
    message_length = len(msg)
    player.conn.sendall(message_length.to_bytes(4, byteorder='big') + msg.encode())

def recv():
    message_length = int.from_bytes(player.conn.recv(4), byteorder='big')
    return player.conn.recv(message_length).decode()

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
