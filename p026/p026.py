def f1(max,digits):
    d = 1
    lend = 1
    one = 10**digits
    for i in range(3,max,2):
        if i % 5:
            inv = str((one/i))
            for j in range(1,digits+1):
                patt = inv[:j]
                rep = int(digits/j) + 1
                mat = (patt*rep)[:len(inv)]
                if mat == inv:
                    if len(patt) > lend:
                        d = i
                        lend = len(patt)
                    break

    return [d, lend]

#-------------------------------------------------------------------------#

res = f1(1000, 1000)
print(res)
