#!/usr/bin/python

#------------------------------------------------------------------------------#

def f1(num):
    s1 = 0
    for i in range(num+1):
        s1 += i * i

    s2 = num * (num + 1)/2
    s2 = int(s2 * s2)

    return s2 - s1

#------------------------------------------------------------------------------#

def f2(num):
    return sum(range(num+1)) ** 2 - sum([x**2 for x in range(num+1)])

#------------------------------------------------------------------------------#

for i in range(1):
    res = f1(100)

print(res)