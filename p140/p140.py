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

    def dis(n):
        return 5*n**2 + 14*n + 1


    tot = 0
    n = 1
    nnug = 0
    while True:
        n += 1
        disn = issquare(dis(n))
        if disn:
            nnug += 1
            tot += n
        if nnug >= nmax:
            break

    print(tot)

def f1(nmax):
    print("--- f1 ---")

    def issquare(k2):
        k = int(math.sqrt(k2))
        if k**2 == k2:
            return k
        return False

    def dis(k):
        return 5*k**2 + 44


    tot = 0
    k = 1
    nnug = 0
    while True:
        k += 1
        disk2 = dis(k)
        disk = issquare(disk2)
        if disk:
            if not (disk - 7) % 5:
                n = (disk - 7)/5
                nnug += 1
                tot += n
        if nnug >= nmax:
            break

    print(tot)

def f2(nmax):
    print("--- f2 ---")

    ks = []

    G, G1 = 4, 1
    # skip 2:
    for j in range(2):
        G, G1 = G + G1, G

    # Get 15 first G(2i+1):
    for i in range(nmax/2):
        G, G1 = G + G1, G
        ks.append(G)

        # skip 3:
        for j in range(3):
            G, G1 = G + G1, G

    ks.append(7)

    H, H1 = 12, 7
    # skip 2:
    for j in range(2):
        H, H1 = H + H1, H

    # Get 15 first H(2i-1):
    for i in range(nmax/2-1):
        H, H1 = H + H1, H
        ks.append(H)

        # skip 2:
        for j in range(3):
            H, H1 = H + H1, H

    ks.sort()

    tot = 0
    for k in ks:
        n = (math.sqrt(5*k**2+44) - 7)/5
        tot += int(n)

    print(tot)


#------------------------------------------------------------------------------#

times = []
for i in [2]:
    t = timeit.Timer('f{0}(30)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  nmax  t (ms)
#         4       0.27
#         8       9.9
#        16      69
#        20    2745
# too slow

# f1:  nmax  t (ms)
#         4       0.44
#         8       9.5
#        16     140
#        20    6200
# too slow

# f2:  nmax  t (ms)
#         4       0.12
#         8       0.14
#        16       0.24
#        20       0.21
#        30       0.36

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
