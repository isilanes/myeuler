import math
import timeit

#------------------------------------------------------------------------------#

def f0(nmax):
    print("--- f0 ---")

    for n in range(1,nmax+1):
        print n
        dmin = int(math.sqrt(n)/2)
        dmax = int((n+1)/4)
        for d in range(dmin,dmax+1):
            s = d**2 - n/2
            if s > 0:
                rs = int(math.sqrt(s))
                if rs**2 == s:
                    y = d + rs
                    if y - d > 0:
                        print n, y + d, y, y - d
                    y = d - rs
                    if y - d > 0:
                        print n, y + d, y, y - d


#------------------------------------------------------------------------------#

times = []
for i in [0]:
    t = timeit.Timer('f{0}(27)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  nmax  t (ms)
#         2

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
