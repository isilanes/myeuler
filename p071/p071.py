#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    r = 3.0/7

    min_tuple = (1.0, None, None)
    Nmax = 1000*1000
    for N in range(1,Nmax+1):
        if not N % 7:
            A = 3*N/7 - 1
        else:
            A = int(3.0*N/7)

        diff = r - float(A)/N
        if diff < min_tuple[0]:
            min_tuple = (diff, A, N)

    print min_tuple

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0(): ~ 0.8 s
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
