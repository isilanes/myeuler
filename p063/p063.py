#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    # i**1 is a 1-digit number for i in range(1,10):
    ndn = 9

    # In i**n, the max value of i is 9. For i > 9 i**n will always have
    # more than n digits.
    imax = 9

    # For 9**n, the resulting number will have n digits for n up to 21.
    # From n = 22 on, 9**2 will always have less than n digits. Obviously
    # for i**n where i < 9, the max n would be lower.
    nmax = 21

    for i in range(2,imax+1):
        for n in range(2,nmax+1):
            x = i**n
            ndigits = len(str(x))
            if ndigits == n:
                ndn += 1
            elif ndigits > n:
                break

    print(ndn)

#--------------------------------------------------------------------#

def f2():
    '''
    From mie00 on projecteuler.net/thread=63;page=8
    '''
    print("--- f2 ---")

    from math import log
    print sum((int(1/(1-log(x,10))) for x in range(1,10)))

#--------------------------------------------------------------------#

import timeit

# f1():
t = timeit.Timer('f1()', "from __main__ import f1")
t1 = t.timeit(number=1)

# f2():
t = timeit.Timer('f2()', "from __main__ import f2")
t2 = t.timeit(number=1)

print("\nTimes:\n")
print('t1 = {0:.2f} ms'.format(t1*1000)) # 0.2 ms
print('t2 = {0:.2f} ms'.format(t2*1000)) # 0.1 ms
