'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5*2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import math

#------------------------------------------------------------------------------#

def f1(tot):
    limit = int(tot/(2+math.sqrt(2)))
    for a in range(1, limit):
        limit2 = int((tot -a)/2)
        for b in range(limit, limit2):
            c = tot - a - b
            if a**2 + b**2 == c**2:
                return a*b*c

#------------------------------------------------------------------------------#

for i in range(1):
    res = f1(1000)

print(res)
