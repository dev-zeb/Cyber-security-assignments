def sockMerchant(n, ar):
    c = 0
    d = dict()
    for i in ar:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    for v in d.values():
        c += v//2
    
    return c

c = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
print("Pair counts: ", c)

c = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
print("Pair counts: ", c)

