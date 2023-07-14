import socket
import time
from Skat import *

print("Welcome to Skat!")
player = Player(input("What would you like to be called?")[:-1])

def main():
       
    get_connected()
    while True:
        next_thing = recv()

        if next_thing == "deal":
            recieve_hand()
        elif next_thing == "bid":
            bidding()
        


def recieve_hand():
    ids = recv()
    player.hand = [get_card(id) for id in ids.split(",")]
    player.printHand()

def bidding():
    pass

def get_connected():
    global conn
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("localhost", 8000))
    name = player.name
    print()
    conn.sendall(name.encode())

def recv():
    data = conn.recv(1024).decode()
    return data


if __name__ == "__main__":
    main()