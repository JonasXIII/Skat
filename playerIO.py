def getBiddingOkay(player, biddingNum):
    while True:
        answer = input(f"{player.name} is {biddingNum} acceptable? {{y/n}}")
        if answer in {"y","Y","yes","Yes"}:
            return True
        if answer in {"n","N","no", "No"}:
            return False
        
def getSuitToPlay(player):
    while True:
        answer = input(f"{player.name} what would you like trump to be? 
        {{1:Blue}} {{2:Green}} {{3:Red}} {{4:Yellow}} {{5:Grand}} {{6:Null}}")