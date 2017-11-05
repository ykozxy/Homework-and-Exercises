#[1 5 10 25]    63
#[1 10 25]  30

# exceed time limit
def min_coin_0(coinlst, n):
    # coinlst.sort(reverse=True)
    minnum = n
    if n in coinlst:
        return 1
    else:
        for i in [c for c in coinlst if c < n]:
            num = 1 + min_coin_0(coinlst, n - i)
            if num < minnum:
                minnum = num
    return minnum


lst =[0] * 400
def min_coin(coinlst, n):
    global lst
    minnum = n
    if n in coinlst:
        lst[n] = 1
        return 1
    elif lst[n] > 0:
        return lst[n]
    else:
        for i in [c for c in coinlst if c < n]:
            num = 1 + min_coin(coinlst, n - i)
            #lst[n] = num
            if num < minnum:
                minnum = num
                lst[n] = minnum
    return minnum






print(min_coin_0([1, 10, 25], 300))
