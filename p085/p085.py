#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def R(N,M):
        return M*(M+1)*N*(N+1)/4

    ref = 2000*1000

    # Max N -> M = 1:
    N = 1
    while True:
        r = R(N,1)
        if r > ref:
            break
        N += 1

    Nmax = N

    min_d = ref
    min_nm = None
    for N in range(1,Nmax+1):
        for M in range(1,N+1):
            r = R(N,M)
            d = abs(r - ref)
            if d < min_d:
                min_d = d
                min_nm = (N,M)
            if r > ref:
                break

    print min_nm, min_nm[0]*min_nm[1]

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 0.7 s
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
