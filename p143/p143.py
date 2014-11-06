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


    c = 511
    for xc in range(500):
        for yc in range(500):
            b = issquare(xc**2 + yc**2)
            if b:
                a = issquare(b**2+c**2-2*c*xc)
                if a:
                    print a, b, c


#------------------------------------------------------------------------------#

times = []
for i in [0]:
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0: too naive, too slow

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
