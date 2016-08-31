# -*- coding=utf-8 -*-

import timeit
from datetime import datetime

def f0(n, disp=True):

    if disp:
        print("--- f0 ---")

    def build_s(n):
        """Return s(k) for k in range(1,N+1), as array.
        N = n*(n+1)/2, that is, "n" is the amount of lines,
        and N is the amount of numbers.
        Technically, s(k) would be s[k-1] here: s(1) is the 
        first (zero) element of the array this function returns.
        """
        s = []
        t = 0
        for k in range(n*(n+1)//2):
            t = (615949*t + 797807) % 1048576 # 2**20 = 1048576
            s.append(t - 524288) # 2**19 = 524288

        return s

    def subt(triang,i,j,k):
        if k == 0:
            return triang[i][j]
        else:
            return subt(triang,i,j,k-1) + sum(triang[i+k][j:j+k+1])


    # Build triangle:
    s = build_s(n)

    k = 0
    triang = []
    for i in range(n):
        triang.append([])
        for j in range(i+1):
            triang[-1].append(s[k])
            k += 1

    # Find the sums of all subtriangles:
    ms = 0
    start = datetime.now()
    for i in range(n):
        now = datetime.now()
        for j in range(i+1):
            for k in range(n-i):
                ret = subt(triang,i,j,k)
                if ret < ms:
                    ms = ret
        end = datetime.now()
        dt = (end - now).total_seconds()
        dt0 = (end - start).total_seconds()

    if disp:
        print(ms)

    return ms

def f1(n, disp=True):
    """Same as f0, with memoization.
    Works, but uses INSANE amounts of memory, plus still too slow."""

    if disp:
        print("--- f1 ---")

    def memoize(f):
        cache = {}
        def helper(tr,i,j,k):
            if (i,j,k) not in cache:
                cache[(i,j,k)] = f(tr,i,j,k)

            return cache[(i,j,k)]


        return helper

    def build_s(n):
        """Return s(k) for k in range(1,N+1), as array.
        N = n*(n+1)/2, that is, "n" is the amount of lines,
        and N is the amount of numbers.
        Technically, s(k) would be s[k-1] here: s(1) is the 
        first (zero) element of the array this function returns.
        """
        s = []
        t = 0
        for k in range(n*(n+1)//2):
            t = (615949*t + 797807) % 1048576 # 2**20 = 1048576
            s.append(t - 524288) # 2**19 = 524288

        return s

    @memoize
    def subt(triang,i,j,k):
        if k == 0:
            return triang[i][j]
        else:
            return subt(triang,i,j,k-1) + sum(triang[i+k][j:j+k+1])


    # Build triangle:
    s = build_s(n)

    k = 0
    triang = []
    for i in range(n):
        triang.append([])
        for j in range(i+1):
            triang[-1].append(s[k])
            k += 1

    # Find the sums of all subtriangles:
    ms = 0
    start = datetime.now()
    for i in range(n):
        now = datetime.now()
        for j in range(i+1):
            for k in range(n-i):
                ret = subt(triang,i,j,k)
                if ret < ms:
                    ms = ret
        end = datetime.now()
        dt = (end - now).total_seconds()
        dt0 = (end - start).total_seconds()
        #print(i, ms, 'dt=', dt, 'total:', dt0)

    if disp:
        print(ms)

    return ms


#------------------------------------------------------------------------------#

if __name__ == "__main__":
    times = []
    for i in [0,1]:
        t = timeit.Timer('f{0}(200)'.format(i), "from __main__ import f{0}".format(i))
        times.append([i, t.timeit(number=1)])

    # Python 3.4.3 times (Burns)
    #
    #    n     res(n)  function  time (ms)
    #
    #    2    -153582        f0        0.2
    #                        f1        0.1
    #
    #   10   -1495491        f0        0.4
    #                        f1        0.4
    #
    #  100  -38951741        f0       3600
    #                        f1        350
    #
    #  200  -87957828        f0      81500
    #                        f1       3300

    # PyPy 5.1.1 @ Python 2.7.10 times (Skinner)
    #
    #    n     res(n)  function  time (ms)
    #
    #  200  -87957828        f0      24400
    #                        f1       3100

    print("\nTimes:\n")
    for i,t in times:
        if t < 2:
            print('t(f{i}) = {t:.1f} ms'.format(i=i, t=t*1000))
        else:
            print('t(f{i}) = {t:.1f} s'.format(i=i, t=t))
