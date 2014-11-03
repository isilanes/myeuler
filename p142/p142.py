import math
import timeit

#------------------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def issquare(k2):
        k = int(math.sqrt(k2))
        if k**2 == k2:
            return k
        return False


    for x in range(3,10**5):
        print(x)
        for y in range(2,x):
            for z in range(1,y):
                if issquare(x+y) and issquare(x-y):
                    if issquare(x+z) and issquare(x-z):
                        if issquare(y+z) and issquare(y-z):
                            print(x+y+z)
                            return

def f1():
    print("--- f1 ---")

    def issquare(k2):
        k = int(math.sqrt(k2))
        if k**2 == k2:
            return k
        return False


    for k in range(3,1000):
        k2 = k**2
        for b in range(2,k):
            B = b**2
            for a in range(1,b):
                A = a**2
                if not (k2 - A - B) % 2:
                    z = (k2 - A - B)/2
                    if issquare(B-A):
                        if issquare(k2-A) and issquare(k2-B):
                            y = z + A
                            x = z + B
                            print(x+y+z)
                            return


#------------------------------------------------------------------------------#

times = []
for i in [1]:
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0: too naive, too slow

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
