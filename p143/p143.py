import math
import timeit

#------------------------------------------------------------------------------#

def f0(ocmax):
    print("--- f0 ---")

    def issquare(k2):
        k = int(math.sqrt(k2))
        if k**2 == k2:
            return k
        return False


    set_oc = set()
    c = 3
    while True:
        c += 1
        for b in range(c/2,c):
            for a in range(c-b,b):
                if 3*a**2 > 2*ocmax**2:
                    break

                k2 = 3*((2*b*c)**2 - (b**2+c**2-a**2)**2)

                if k2 < 0:
                    continue

                k = issquare(k2)
                if k:
                    oc2 = (c**2 + b**2 + a**2 + k)/2
                    if oc2 > ocmax**2:
                        break
                    oc = issquare(oc2)
                    if oc and oc < ocmax:
                        set_oc.add(oc)
            if 2*b**2 > 2*ocmax**2:
                break
        if c**2 > 2*ocmax**2:
            break

    print(sum(set_oc))

def f1(ocmax):
    print("--- f1 ---")

    def issquare(k2):
        k = int(math.sqrt(k2))
        if k**2 == k2:
            return k
        return False


    set_oc = set()
    for r in range(1, ocmax):
        r2 = r**2
        for q in range(r+1, ocmax-r):
            q2 = q**2
            a = issquare(r2 + q2 + r*q)
            if a:
                for p in range(q+1, ocmax-r-q):
                    p2 = p**2
                    b = issquare(q2 + p2 + p*q)
                    if b:
                        c = issquare(p2 + r2 + r*p)
                        if c:
                            pqr = p + q + r
                            if pqr < ocmax:
                                set_oc.add(pqr)
                                print r, (a, b, c)

    print(sum(set_oc))


#------------------------------------------------------------------------------#

times = []
for i in [1]:
    t = timeit.Timer('f{0}(120000)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0: wrong
# f1: ~ 142 s

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
