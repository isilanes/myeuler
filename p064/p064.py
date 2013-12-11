#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import math

    N = 23
    sN = math.sqrt(N)
    a0 = int(sN)

    print a0
    old = a0
    for i in range(10):
        r = (sN + old) / (N - old**2)
        a = int(r)
        print(a)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
