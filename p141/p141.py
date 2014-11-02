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


    kmax = int(math.sqrt(nmax))

    progs = set([])
    for k in range(1,kmax+1):
        n = k**2
        for d in range(2,k):
            q = n // d
            r = n % d
            if q*r == d**2:
                progs.add(n)
                print(n)

    print ">", sum(progs)

def f1(rmax):
    print("--- f1 ---")

    def issquare(k2):
        k = int(math.sqrt(k2))
        if k**2 == k2:
            return k
        return False


    progs = []
    r = 1
    while True:
        for alpha in range(2,120):
            for beta in range(1,alpha):
                if not alpha*r % beta: # integer p
                    if not alpha**2*r % beta**2: # inger q
                        n = alpha**3*r**2/beta**3 + r
                        if not n in progs and n < rmax and issquare(n):
                            progs.append(n)

        r += 1
        if r**2 >= rmax:
            break

    print(sum(progs))


#------------------------------------------------------------------------------#

times = []
for i in [1]:
    t = timeit.Timer('f{0}(10**12)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  nmax    t (ms)
#     10**4         4.5
#     10**6        30
#     10**8      1949
#    10**10    214030
#    10**12  too slow

# f1:  nmax  t (ms)
#     10**4     165
#     10**6     333
#     10**8    2745
#    10**10   31350
#    10**12  467400

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
