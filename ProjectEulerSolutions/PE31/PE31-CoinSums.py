# PROJECT EULER PROBLEM 31 - Coin Sums

COINS = [200,100,50,20,10,5,2,1]
LEN_COINS = len(COINS)

target_amount = 200

def countCoinCombos(coin_list,amount):
    coin = coin_list[0]
    new_coin_list = coin_list[1:]
    n = 0
    count = 0 # count of combinations of coins
    coin_amount = 0
    while coin_amount <= amount:
        #out_str = ''
        #for q in range(LEN_COINS-len(new_coin_list)-1):
        #    out_str += "\t"
        #out_str += "{} x {}".format(coin,n)
        new_amount = amount - coin_amount
        if new_amount == 0:
            count += 1
            #print(out_str)
        elif new_amount > 0:
            if len(new_coin_list) != 0:
                #print(out_str)
                count += countCoinCombos(new_coin_list,new_amount)
        n += 1
        coin_amount = n*coin
    return(count)

print(countCoinCombos(COINS,target_amount))

