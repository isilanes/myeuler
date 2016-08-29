# -*- coding=utf-8 -*-

import math
import timeit
import numpy as np

def memoize(f):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = f(x)

        return cache[x]


    return helper

@memoize
def s(k):
    if k < 56:
        return (100003 - 200003*k + 300007*k**3) % 1000000 - 500000
    else:
        return (s(k-24) + s(k-55) + 1000000) % 1000000 - 500000

def f0(n, disp=True):
    """Generates an n*n square. n=2000 for original problem."""

    if disp:
        print("--- f0 ---")

    def max_sum(a):
        """Take list "a" and return largest sum of consecutive elements."""

        mx = -999999

        for i in range(len(a)):
            if a[i] < 0:
                continue
            for j in range(i, len(a)):
                if a[j] < 0:
                    continue
                v = sum(a[i:j+1])
                if v > mx:
                    mx = v

        return mx


    # Check it works correctly:
    assert s(10) == -393027
    assert s(100) == 86613

    # Generate board:
    a = [ s(i) for i in range(1,n*n+1) ]
    a = np.array(a).reshape((n,n))

    # Check horizontal rows:
    for row in a:
        max_h = max_sum(row)

    # Check vertical columns:
    for col in a.T:
        max_v = max_sum(col)

    ret = max(max_h, max_v)
    print(ret)

    return ret

def f1(n, disp=True):
    """Generates an n*n square. n=2000 for original problem."""

    if disp:
        print("--- f1 ---")

    def max_sum(a):
        """Take list "a" and return largest sum of consecutive elements."""

        mx = -999999

        for i,ai in enumerate(a):
            if ai < 0:
                continue
            for j,aj in enumerate(a[i:]):
                if aj < 0:
                    continue
                v = sum(a[i:j+i+1])
                if v > mx:
                    mx = v

        return mx


    # Check it works correctly:
    assert s(10) == -393027
    assert s(100) == 86613

    # Generate board:
    a = [ s(i) for i in range(1,n*n+1) ]
    a = np.array(a).reshape((n,n))

    # Check horizontal rows:
    for row in a:
        max_h = max_sum(row)

    # Check vertical columns:
    for col in a.T:
        max_v = max_sum(col)

    ret = max(max_h, max_v)
    print(ret)

    return ret

def f2(n, disp=True):
    """Generates an n*n square. n=2000 for original problem."""

    if disp:
        print("--- f2 ---")

    def max_sum(a):
        """Take list "a" and return largest sum of consecutive elements."""

        b = []
        pos = True
        if a[0] < 0:
            pos = False

        cum = 0
        for e in a:
            if (e > 0) == pos:
                cum += e
            else:
                b.append(cum)
                cum = e
                pos = not pos

        mx = -999999

        a = b
        for i,ai in enumerate(a):
            if ai < 0:
                continue
            for j,aj in enumerate(a[i:]):
                if aj < 0:
                    continue
                v = sum(a[i:j+i+1])
                if v > mx:
                    mx = v

        return mx


    # Check it works correctly:
    assert s(10) == -393027
    assert s(100) == 86613

    # Generate board:
    a = [ s(i) for i in range(1,n*n+1) ]
    a = np.array(a).reshape((n,n))
    ms = 0

    # Check horizontal rows:
    for row in a:
        ret = max_sum(row)
        if ret > ms:
            ms = ret

    # Check vertical columns:
    for col in a.T:
        ret = max_sum(col)
        if ret > ms:
            ms = ret

    print(a)
    # Check diagonals:
    for i in range(n):
        diag = [ a[k,i-k] for k in range(i+1) ]
        print(diag)
    for j in range(1,n):
        diag = [ a[n-k,k] for k in range(j,n) ]
        print(diag)
    exit()

    if disp:
        print(ms)

    return ms


#------------------------------------------------------------------------------#

if __name__ == "__main__":
    times = []
    for i in [0,1,2]:
        t = timeit.Timer('f{0}(8)'.format(i), "from __main__ import f{0}".format(i))
        times.append([i, t.timeit(number=1)])

    # Python 3.x times #

    #   n   res(n)  function  time (ms)
    # 100  3552499        f0      ~1500
    #                     f1      ~1400
    #                     f2       ~150

    print("\nTimes:\n")
    for i,t in times:
        if t < 2:
            print('t(f{i}) = {t:.1f} ms'.format(i=i, t=t*1000))
        else:
            print('t(f{i}) = {t:.1f} s'.format(i=i, t=t))
