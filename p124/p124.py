#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def get_rad(n):
        rads = []
        if not n % 2:
            rads.append(2)
            while not n % 2:
                n = n / 2
        i = 3
        while n > 1:
            if not n % i:
                rads.append(i)
                while not n % i:
                    n = n / i
            i += 2
        
        rad = 1
        for e in rads:
            rad = rad*e
        return rad
    
    dsu = []
    for n in range(1,10**5+1):
        rad = get_rad(n)
        dsu.append([rad, n])
    dsu.sort()

    print(dsu[10**4-1][1])

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 8.6 s (pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
