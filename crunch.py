biddingOrder = [18,27,36,45,54,63,72,81,90,99,108,117,126,135,144,153,162,171,180,189,198,207,216,225,234,243,
                20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,
                22,33,44,55,66,77,88,99,110,121,132,143,154,165,176,187,198,209,220,231,242,
                24,36,48,60,72,84,96,108,24,48,72,96,120,144,168,192,216,240]
print(biddingOrder)
biddingOrder.sort()
print(biddingOrder)

res = [*set(biddingOrder)]
print(res)
res.sort()
print(res)