from playerIO import *
from colorama import init

init()

class Card: 
    def __init__(self, name, suit, rank, eyes, id):
        self.name = name
        self.suit = suit
        self.rank = rank
        self.eyes = eyes
        self.id = id

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

class Player:
    def __init__(self, name, conn, addr):
        self.name = name
        self.hand = []
        self.conn = conn
        self.addr = addr

    def printHand(self):
        print(f"{self.hand}")
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def getHand(self):
        ret = ""
        for card in self.hand:
            ret += card.name + ","
        return ret[:-1]

def get_card(id):
    for card in ALL_CARDS:
        if card.id == int(id):
            return card
    return id


BIDDING_ORDER = [18, 20, 22, 23, 24, 27, 30, 33, 35, 36, 40, 44, 45, 46, 48, 50, 54, 55, 59, 60, 63, 66, 70, 72, 77, 80, 81, 84, 88, 90, 96, 99, 100, 108, 110, 117, 120, 121, 126, 130, 132, 135, 140, 143, 144, 150, 153, 154, 160, 162, 165, 168, 170, 171, 176, 180, 187, 
189, 190, 192, 198, 200, 207, 209, 210, 216, 220, 225, 230, 231, 234, 240, 242, 243, 250]
ALL_CARDS = [    
    Card("\u001b[33m7\u001b[0m", 's', '7', 0, 0), Card("\u001b[33m8\u001b[0m", 's', '8', 0, 1), Card("\u001b[33m9\u001b[0m", 's', '9', 0, 2), 
    Card("\u001b[33mO\u001b[0m", 's', 'O', 3, 3), Card("\u001b[33mK\u001b[0m", 's', 'K', 4, 4), Card("\u001b[33m1\u001b[0m", 's', '1', 10, 5), 
    Card("\u001b[33mA\u001b[0m", 's', 'A', 11, 6),
    
    Card("\033[91m7\u001b[0m", 'r', '7', 0, 7), Card("\033[91m8\u001b[0m", 'r', '8', 0, 8), Card("\033[91m9\u001b[0m", 'r', '9', 0, 9), 
    Card("\033[91mO\u001b[0m", 'r', 'O', 3, 10), Card("\033[91mK\u001b[0m", 'r', 'K', 4, 11), Card("\033[91m1\u001b[0m", 'r', '1', 10, 12), 
    Card("\033[91mA\u001b[0m", 'r', 'A', 11, 13),

    Card("\u001b[32m7\u001b[0m", 'g', '7', 0, 14), Card("\u001b[32m8\u001b[0m", 'g', '8', 0, 15), Card("\u001b[32m9\u001b[0m", 'g', '9', 0, 16), 
    Card("\u001b[32mO\u001b[0m", 'g', 'O', 3, 17), Card("\u001b[32mK\u001b[0m", 'g', 'K', 4, 18), Card("\u001b[32m1\u001b[0m", 'g', '1', 10, 19), 
    Card("\u001b[32mA\u001b[0m", 'g', 'A', 11, 20), 
    
    Card("\u001b[34m7\u001b[0m", 'e', '7', 0, 21), Card("\u001b[34m8\u001b[0m", 'e', '8', 0, 22), Card("\u001b[34m9\u001b[0m", 'e', '9', 0, 23), 
    Card("\u001b[34mO\u001b[0m", 'e', 'O', 3, 24), Card("\u001b[34mK\u001b[0m", 'e', 'K', 4, 25), Card("\u001b[34m1\u001b[0m", 'e', '1', 10, 26), 
    Card("\u001b[34mA\u001b[0m", 'e', 'A', 11, 27),
    
    Card("\u001b[33mU\u001b[0m", 's', 'U', 2, 28),Card("\033[91mU\u001b[0m", 'r', 'U', 2, 29),
    Card("\u001b[32mU\u001b[0m", 'g', 'U', 2, 30),Card("\u001b[34mU\u001b[0m", 'e', 'U', 2, 31), 
]





                    
def getGameType(solo, hand):
    good = False
    while not good:
        gametype = input(f"{solo} what kind of game would you like to play?\nE\nG\nR\nS\nGrand\nNull\n")
        if gametype in {"E", "G", "R", "S", "Grand", "Null"}:
            good = True
    






def playGame(deck, pos1, pos2, pos3):
    print("starting game")
    deal(deck,pos1,pos2,pos3)
    winningBid, soloPlayer = bidding(pos1,pos2,pos3)
    if soloPlayer == None:
        print("No one wants to be the solo-player, so no game.")
        return
    print(f"{soloPlayer} is the solo player with a winning bid of {biddingOrder[winningBid]}.")
    #gameType = getGameType(soloPlayer)

    


# playGame(allCards, player1, player2,player3)