#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def period(a):
        '''
        Returns periodicity for a.
        '''
        k = 1
        while True:
            r = ( (a-1)**(k+1) + (a+1)**(k+1) - 2*a) % a**2
            if r == 0:
                return k
            k += 1

    tot = 0
    for a in range(3,1001):
        # Find periodicity:
        k = period(a)

        # Then check only n in range {1, k+1}:
        rmax = 0
        for n in range(1,k+2):
            r = ( (a-1)**n + (a+1)**n ) % a**2
            if r > rmax:
                rmax = r
        tot += rmax

    print(tot)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 55 s (pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
