def getBiddingOkay(player, biddingNum):
    while True:
        answer = input(f"{player.name} is {biddingNum} acceptable? {{y/n}}")
        if answer in {"y","Y","yes","Yes"}:
            return True
        if answer in {"n","N","no", "No"}:
            return False