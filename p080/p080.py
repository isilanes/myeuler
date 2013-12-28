#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import decimal as dec
    dec.getcontext().prec = 110
    dec.getcontext().rounding = dec.ROUND_DOWN

    Nmax = 100
    
    # Find all squares up to Nmax:
    i = 1
    squares = []
    while i*i < Nmax + 1:
        squares.append(i*i)
        i += 1

    # Loop over all sqrts, and add decimals as requested:
    total = 0
    for N in range(1,Nmax+1):
        if not N in squares:
            N = dec.Decimal(N)
            s = N.sqrt()
            s = s*10**100
            s = str(s)[:100]
            s = sum([ int(x) for x in s ])

            total += s

    # Final result:
    print(total)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 23 ms
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
