import random



def comp(card):
    return card.id

def deal(cards,player1,player2,player3, seed):
    random.seed(seed)
    
    player1.hand = []
    player2.hand = []
    player3.hand = []
    skat = []
    random.shuffle(cards)
    for i, card in enumerate(cards):
        if i < 10:
            player1.hand.append(card)
        elif i < 20:
            player2.hand.append(card)
        elif i < 30:
            player3.hand.append(card)
        else:
            skat.append(card)
    
    player1.hand.sort(key=comp)
    player2.hand.sort(key=comp)
    player3.hand.sort(key=comp)
    return skat
