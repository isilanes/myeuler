#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def iskosher(n,m):
        '''
        Check whether n**m = N, where N's digits add up to n.
        '''

        N = n**m
        digs = [ int(x) for x in str(N) ]
        return sum(digs) == n

    # a1  =              81 = 9**2
    # a2  =             512 = 8**3
    # a10 =          614656 = 28**4
    # a30 = 248155780267521 = 63**8
    valids = []
    for n in range(2,100):
        for m in range(2,12):
            if iskosher(n,m):
                valids.append([n**m, n,m])
        if len(valids) > 40:
            break

    valids.sort()
    print(valids[29])

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 5.5 ms (python3)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
