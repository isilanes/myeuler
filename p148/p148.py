# -*- coding=utf-8 -*-

import math
import timeit
import numpy as np

def display(nlines):

    s = {
        1: ".",
        2: ".",
        3: ".",
        4: ".",
        5: ".",
        6: ".",
        7: ".",
        8: ".",
        9: ".",
        0: "0",
    }

    ndiv = 1
    old_line = [1]
    for i in range(2,nlines+1):
        line = np.zeros(i, dtype=np.int)
        line[:-1] = old_line
        line[1:] = (line[1:] + old_line) % 7
        line[-1] = 1
        old_line = line
        string = "{i:3} ".format(i=i) + "".join([s[x] for x in line])
        print(string)

def f0(nlines, disp=True):

    if disp:
        print("--- f0 ---")

    ndiv = 1 # first line
    line = []
    for i in range(nlines-1):
        newline = [ a+b for a,b in zip(line, line[1:]) ]
        newline = [1] + newline + [1]
        line = newline
        ndiv += sum([ 1 for k in line if k % 7 ])

    if disp:
        print(ndiv)

    return ndiv

def f1(nlines, disp=True):

    if disp:
        print("--- f1 ---")

    ndiv = 1 # first line
    line = [ 0 for i in range(nlines) ]
    line[0] = 1
    for i in range(2,nlines+1):
        line[i-1] = 1
        for j in range(i-2,0,-1):
            line[j] += line[j-1]
        ndiv += sum([ 1 for k in line if k % 7 ])

    if disp:
        print(ndiv)

    return ndiv

def f2(nlines):

    print("--- f2 ---")

    ndiv = 1 # first line
    line = np.zeros(nlines, dtype=np.int)
    line[0] = 1
    for i in range(2,nlines+1):
        line[i-1] = 1
        for j in range(i-2,0,-1):
            line[j] = (line[j] + line[j-1]) % 7
        ndiv += np.count_nonzero(line)

    print(ndiv)

    return ndiv

def f3(nlines):

    print("--- f3 ---")

    ndiv = 1 # first line
    line = np.zeros(nlines, dtype=np.int)
    line[0] = 1
    for i in range(2,nlines+1):
        line[1:i] = (line[1:i] + line[:i-1]) % 7
        ndiv += np.count_nonzero(line)

    print(ndiv)

    return ndiv

def f4(nlines, disp=True):

    if disp:
        print("--- f4 ---")

    ndiv = 1
    old_line = [1]
    for i in range(2,nlines+1):
        line = np.zeros(i, dtype=np.int)
        line[:-1] = old_line
        line[1:] = (line[1:] + old_line) % 7
        line[-1] = 1
        ndiv += np.count_nonzero(line)
        old_line = line

    if disp:
        print(ndiv)

    return ndiv

def f5(nlines, disp=True):
    """Very fast, but only for nlines = 7**n."""

    if disp:
        print("--- f5 ---")

    def T(n):
        return (7**(2*n) - 7**n)//2

    def C(n):
        if n == 0:
            return 0
        else:
            return 7*C(n-1) + 21*(T(n) + C(n-1))


    n = int(round(math.log(nlines, 7)))

    ndiv = ((nlines+1)*nlines)//2 - C(n-1)

    if disp:
        print(ndiv)

    return ndiv

def f6(nlines):
    """Evolution of f5(), for any nlines.
    Doesn't scale well, due to not developing some summatories."""

    print("--- f6 ---")

    def D(n):
        return (49**n - 7**n)/2

    def DT(n,j):
        """Same as D(n), but truncated at j lines."""

        res = 0
        for i in range(1,j+1):
            res += 7**n - i

        return res

    def T(n):
        if n <= 1:
            return 0
        else:
            return 28*T(n-1) + 21*D(n-1)

    def TT(n,j):
        """Same as T(n), but truncated at j lines."""

        if n == 0 or j == 0:
            return 0
        else:
            tnm1 = T(n-1)
            dnm1 = D(n-1)

            # Up to largest linecount for 7**n, integer n:
            p1 = tnm1

            # Full 7**n-size "line blocks" up to truncation of 7**(n+1) triangle:
            p2 = 0
            beta = j // (7**(n-1))
            for i in range(1, beta):
                p2 += (1 + i) * tnm1 + i * dnm1

            # Truncated line:
            x = j - beta*7**(n-1)
            p3 = (1+beta)*TT(n-1, x) + beta*DT(n-1, x)

            return p1 + p2 + p3


    tot = ((nlines+1)*nlines)/2 # total numbers
    n = int(math.log(nlines, 7))
    ndiv = tot - TT(n+1, nlines)
    print(ndiv)

    return ndiv

def f7(nlines, disp=True):
    """Evolution of f6(), for any nlines, no for loops for summatories."""

    if disp:
        print("--- f7 ---")

    def D(n):
        return (49**n - 7**n) // 2

    def DT(n,j):
        """Same as D(n), but truncated at j lines."""

        return j*7**n - (j+1)*j // 2

    def T(n):
        if n <= 1:
            return 0
        else:
            return 28*T(n-1) + 21*D(n-1)

    def TT(j):
        """Same as T(n), but truncated at j lines."""

        if j == 0:
            return 0

        n = int(math.log(j, 7)) + 1

        if n <= 1 or j <= 7:
            return 0
        else:
            tnm1 = T(n-1)
            dnm1 = D(n-1)

            # Up to largest linecount for 7**n, integer n:
            p1 = tnm1

            # Full 7**n-size "line blocks" up to truncation of 7**(n+1) triangle:
            p2 = 0
            beta = j // (7**(n-1))
            for i in range(1, beta):
                p2 += (1 + i) * tnm1 + i * dnm1

            # Truncated line:
            x = j - beta*7**(n-1)
            ttnm1 = TT(x)
            dtnm1 = DT(n-1,x)
            p3 = (1+beta)*ttnm1 + beta*dtnm1

            return p1 + p2 + p3


    tot = ((nlines+1)*nlines) // 2 # total amount of numbers
    ndiv = tot - TT(nlines)

    if disp:
        print(ndiv)

    return ndiv


#------------------------------------------------------------------------------#

if __name__ == "__main__":
    times = []
    for i in [7]:
        t = timeit.Timer('f{0}(10**9)'.format(i), "from __main__ import f{0}".format(i))
        times.append([i, t.timeit(number=1)])

    # function  nlines  ------- time (ms) -------
    #                   python2  python3     pypy
    # f0:          100      1.1      1.2     24.7
    # f0:         1000     ~270    294.2    236.5
    # f0:         2000    ~1400   1305.0   1319.5

    # f1:         1000     ~270     ~251
    # f1:         2000    ~1510    ~1480 

    # f2:         1000     ~275     ~275
    # f2:         2000     ~995     ~910

    # f3:         1000      ~13      ~14 
    # f3:         2000      ~40      ~43 
    # f3:        10000     ~900     ~955 
    # f3:       100000   ~95000   ~98000 

    # f4:         1000               ~25 
    # f4:         2000               ~55 
    # f4:        10000              ~910 
    # f4:        50000            ~25000 
    # f4:       100000           ~101000

    # f6:         1000              <0.1
    # f6:        10000               0.1
    # f6:       100000              ~2.0
    # f6:      1000000               ~39
    # f6:     10000000              ~410
    # f6:    100000000             ~2000

    # f7:         1000              <0.1 
    # f7:        10000              <0.1
    # f7:       100000              <0.1
    # f7:      1000000               0.1
    # f7:     10000000               0.1
    # f7:    100000000               0.1
    # f7:   1000000000               0.2

    print("\nTimes:\n")
    for i,t in times:
        if t < 2:
            print('t(f{i}) = {t:.1f} ms'.format(i=i, t=t*1000))
        else:
            print('t(f{i}) = {t:.1f} s'.format(i=i, t=t))
