#!/usr/bin/python

#-------------------------------------------------------------------------------#

def is_palindrome(x, y):
    s = '{0}'.format(x*y)

    if s == s[::-1]:
        return True
    else:
        return False

#-------------------------------------------------------------------------------#

def f1(max):
    min = 100
    n = max
    sol = [0,0]
    while True:
        pal = is_palindrome(n, max)
        if pal:
            #print(n, max, n*max)
            # Is it largest so far?:
            if n*max > sol[0]*sol[1]:
                sol = [n,max]

            min  = n + 1
            max -= 1
            n    = max
            if not max > min:
                print(sol, sol[0]*sol[1])
                break
        else:
            n -= 1

        if n < min:
            max -= 1
            n    = max


#-------------------------------------------------------------------------------#

for i in range(1):
    f1(999)
