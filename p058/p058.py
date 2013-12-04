#--------------------------------------------------------------------#

def f1(nlayers):
    '''
    Unable to deliver. Too much memory required!
    '''
    print("--- f1 ---")

    max = (nlayers*2-1)**2 - nlayers

    # First populate list of numbers in the diagonals (leave out the
    # lower-right arm, as it contains squares, obviously non-prime):
    diag_nums = {}
    for i in range(2,nlayers+1):
        n = 2*i - 1
        for num in [ n**2-n+1, n**2-2*n+2, n**2-3*n+3 ]:
            diag_nums[num] = True

    # Then use sieve to get all composites below "max", and save only
    # those in diag_nums:
    composites = {}
    nprimes = 0
    for mult in range(3,max,2):
        if not mult in composites:
            if mult in diag_nums:
                nprimes += 1
            for i in range(mult*mult, max, 2*mult):
                composites[i] = True

    # Calculate the percent:
    sidelen = 2*nlayers-1
    perc = 100.0 * nprimes / (4.0 * nlayers - 3)
    print("{0:3d} {1:7.4f}".format(sidelen, perc))

#--------------------------------------------------------------------#

def f2():
    print("--- f2 ---")

    def isprime(num):
        '''
        Returns True if num is prime, False otherwise.
        '''
        if not num % 2:
            return False

        for i in range(3,int(math.sqrt(num)),2):
            if not num % i:
                return False

        return True

    # Proceed with the spiral:
    p = []
    i = 2
    while True:
        n = 2*i - 1
        for num in [ n**2-n+1, n**2-2*n+2, n**2-3*n+3 ]:
            if isprime(num):
                p.append(num)
        perc = 100.0 * len(p) / (2.0 * n - 1.0)
        if perc < 10.0:
            print("{0:3d} {1:7.4f}".format(n, perc))
            break
        i += 1

#--------------------------------------------------------------------#

import math
import timeit

# f1():
#t = timeit.Timer('f1(2000)', "from __main__ import f1")
#t1 = t.timeit(number=1)

# f2():
t = timeit.Timer('f2()', "from __main__ import f2")
t2 = t.timeit(number=1)

print("\nTimes:\n")
#print('t1 = {0:.1f} ms'.format(t1*1000)) # a lot!
print('t2 = {0:.1f} ms'.format(t2*1000)) # ~ 750 ms
