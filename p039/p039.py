def f1():
    maxnum = 3
    maxp = 120
    for p in range(3,1000):
        num = 0
        for a in range(1, int(p/3)):
            a2 = a**2
            for b in range(a+1, int(p/2)):
                if a2 + b**2 == (p - a - b)**2:
                    num += 1

        if num > maxnum:
            maxnum = num
            maxp = p

    return [maxp, maxnum]

#-------------------------------------------------------------------------#

res = f1()
print(res)
