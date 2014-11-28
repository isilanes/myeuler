import timeit

#------------------------------------------------------------------------------#

def f0(M,N):
    print("--- f0 ---")

    # Horizontal rectangles of size m*n, within rectangle of size M*N
    for m in range(1,M+1):
        for n in range(1,N+1):
            c = (M - m + 1) * (N - n + 1)
            print m, "x", n, "=", c


#------------------------------------------------------------------------------#

times = []
for i in [0]:
    t = timeit.Timer('f{0}(3,2)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  maxn   t (ms) - v = 1.0

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
