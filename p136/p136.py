import math
import timeit

#------------------------------------------------------------------------------#

def f0(nmax):
    print("--- f0 ---")

    freq = [ 0 for x in range(nmax+1) ]

    dmax = int((nmax+1)/4)
    for d in range(1, dmax+1):
        fourd = 4*d
        if fourd*d < nmax:
            for y in range(d+1, fourd):
                n = y*(fourd - y)
                if n < nmax:
                    freq[n] += 1
        else:
            rs = int(math.sqrt(fourd*d - nmax))
            for y in range(d+1, 2*d-rs):
                n = y*(fourd - y)
                if n < nmax:
                    freq[n] += 1
            for y in range(2*d+rs, fourd):
                n = y*(fourd - y)
                if n < nmax:
                    freq[n] += 1

    nfreq = 0
    for i,e in enumerate(freq):
        if e == 1:
            nfreq += 1
    print(nfreq)


#------------------------------------------------------------------------------#

times = []
for i in [0]:
    t = timeit.Timer('f{0}(5*10**7)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  nmax  t (ms)
#       100       0.35
#      5000      25
#     50000      31
#    500000     131
#   5000000     800
#  50000000    7550

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
