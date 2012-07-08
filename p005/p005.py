#!/usr/bin/python

#------------------------------------------------------------------------------#

def f1(num):
    factors = [2,3]
    for i in range(4,num):
        j = i
        for factor in factors:
            if not j % factor:
                j = int(j/factor)

        if j > 1:
            factors.append(j)

    res = 1
    for factor in factors:
        res = res * factor

    return res

#------------------------------------------------------------------------------#

for i in range(1):
    res = f1(20)

print(res)
