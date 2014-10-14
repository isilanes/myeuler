import math
import timeit

#------------------------------------------------------------------------------#

def f0(nmax):
    print("--- f0 ---")

    def issquare(k2):
        k = int(math.sqrt(k2))
        if k**2 == k2:
            return k
        return False


    B = 7
    ntriag = 0
    tot = 0
    while True:
        # The plus:
        L2 = 5*B**2 + 4*B + 1

        L = issquare(L2)
        if L:
            tot += L
            ntriag += 1
            if ntriag == nmax:
                break

        # The minus:
        L2 = 5*B**2 - 4*B + 1

        L = issquare(L2)
        if L:
            tot += L
            ntriag += 1
            if ntriag == nmax:
                break
        B += 1

    print(tot)

def f1(nmax):
    print("--- f1 ---")

    def issquare(k2):
        k = int(math.sqrt(k2))
        if k**2 == k2:
            return k
        return False


    L = 2
    ntriag = 0
    tot = 0
    while True:
        rs = 5*L**2 - 1
        r = issquare(rs)
        if r:
            n5 = r - 2 # the minus solution
            if not n5 % 5:
                tot += L
                ntriag += 1
            n5 = r + 2 # the plus solution
            if not n5 % 5:
                tot += L
                ntriag += 1
        L += 1
        if ntriag == nmax:
            break

    print(tot)

def f2(nmax):
    print("--- f2 ---")

    F, F1 = 21, 13
    ntriag = 0
    tot = 0
    while True:
        F, F1 = F+F1, F
        ntriag += 1
        tot += F/2
        if ntriag == nmax:
            print(tot)
            break

        # Skip 5:
        for i in range(5):
            F, F1 = F+F1, F

def f3(nmax):
    '''Use Binet's formula to calculate nth Fibonacci number.
    WARNING: too imprecise for large n, and specifically
    for solving this problemn (nmax=12).'''

    print("--- f3 ---")

    phi = (1 + math.sqrt(5))/2

    tot = 0
    for i in range(nmax):
        n = 9 + 6*i
        F = (phi**n - (-phi)**(-n))/math.sqrt(5)
        L = int(F/2)
        tot += L

    print(tot)


#------------------------------------------------------------------------------#

times = []
for i in [2]:
    t = timeit.Timer('f{0}(12)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times:

# f0: 7.5 s for n=7
# f1: 8.2 s for n=7
# f2: 0.16 ms for n=12 <---
# f3: 0.18 ms for n=11, but too imprecise for n=12

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
