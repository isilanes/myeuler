#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import math

    N = 23
    sN = math.sqrt(N)
    a0 = int(sN)

    A = 1
    B = 4

    aa = []
    for i in range(10):
        newA = (N - B**2)/A
        newB = (N - B**2) - (A*B) % (N - B**2)
        ai = A*B / (N - B**2) + 1
        aa.append(ai)
        A, B = newA, newB
        print ai, newA, newB

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
