#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    nval = 0
    n = 3
    maxnval = 0
    while nval < 22:
        n += 1
        xmax = n*(n+1)
        nval = 0
        for x in range(1,xmax+1):
            for y in range(x,xmax+1):
                if n*(x+y) == y*x:
                    nval += 1
        if nval > maxnval:
            print n, ">", nval
            maxnval = nval

#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    nval = 0
    n = 3
    maxnval = 0
    while nval < 1001:
        n += 1
        xmax = n*(n+1)
        nval = 0
        x = n
        while x < xmax:
            x += 1
            y = n*x // (x - n)
            if y < x:
                break
            if n*(x+y) == y*x:
                nval += 1
        if nval > maxnval:
            print n, ">", nval
            maxnval = nval

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(2):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: brutally slow
# f1: pitiful bruteforce, but works (~ 495 s pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
