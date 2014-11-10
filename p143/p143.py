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


#------------------------------------------------------------------------------#

times = []
for i in [0]:
    t = timeit.Timer('f{0}(12000)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0: too naive, too slow

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
