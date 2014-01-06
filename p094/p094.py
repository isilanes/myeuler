#--------------------------------------------------------------------#

def f0(pmax):
    print("--- f0 ---")

    import math

    def issq(N):
        r = int(math.sqrt(N))
        return r*r == N

    sum_peri = 0
    Nmax = int(pmax/3)
    for N in xrange(3,Nmax,2):
        # -1:
        B = (N - 1) / 2
        h2 = N**2 - B**2
        if issq(h2):
            sum_peri += 3*N - 1

        # +1:
        B = (N + 1) / 2
        h2 = N**2 - B**2
        if issq(h2):
            sum_peri += 3*N + 1

    print(sum_peri)

#--------------------------------------------------------------------#

def f1(pmax):
    print("--- f1 ---")

    import math

    def issq(N):
        r = int(math.sqrt(N))
        return r*r == N

    sum_peri = 0
    N = 0
    for i in xrange(2,(pmax+2)/6):
        # -1:
        N = 2*i + 1
        h2 = N**2 - i**2
        if issq(h2):
            sum_peri += 3*N - 1
        
        # +1:
        N = 2*i - 1
        h2 = N**2 - i**2
        if issq(h2):
            sum_peri += 3*N + 1

        i += 1

    print(sum_peri)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(2):
    t = timeit.Timer('f{0}(1000*1000*1000)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 270 s
# f1: ~ 291 s (even slower!)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
