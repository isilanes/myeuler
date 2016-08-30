# -*- coding=utf-8 -*-

import timeit

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

def f0(n, disp=True):
    """Generates an n*n square. n=2000 for original problem."""

    if disp:
        print("--- f0 ---")

    def max_sum(arr):
        """Take list "a" and return largest sum of consecutive elements."""

        mx = -999999

        for i in range(len(arr)):
            if arr[i] < 0:
                continue
            for j in range(i, len(arr)):
                if arr[j] < 0:
                    continue
                v = sum(arr[i:j+1])
                if v > mx:
                    mx = v

        return mx

    def max_horizontal(a):
        """Generate all horizontal rows, and return max sum of any."""

        ms = 0
        for row in a:
            ret = max_sum(row)
            if ret > ms:
                ms = ret

        return ms

    def max_vertical(a):
        """Generate all vertical columns, and return max sum of any."""

        ms = 0
        for col in a.T:
            ret = max_sum(col)
            if ret > ms:
                ms = ret

        return ms

    def max_bltr_diagonals(a,n):
        """Generate all botton-left to top-right type lines, and return max sum of any."""

        ms = 0
        for j in range(n):
            diag = [ a[k,j-k] for k in range(j+1) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        for i in range(1,n):
            diag = [ a[k,i-k+n-1] for k in range(i,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        return ms

    def max_tlbr_diagonals(a,n):
        """Generate all top-left to bottom-right type lines, and return max sum of any."""

        ms = 0
        for i in range(n):
            diag = [ a[k,k-i] for k in range(i,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        for j in range(1,n):
            diag = [ a[k-j,k] for k in range(j,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        return ms


    # Check it works correctly:
    assert s(10) == -393027
    assert s(100) == 86613

    # Generate board:
    a = [ s(i) for i in range(1,n*n+1) ]
    a = np.array(a).reshape((n,n))
    ms = 0

    # Check horizontal rows (will be max so far):
    ms = max_horizontal(a)

    # Check vertical columns:
    ret = max_vertical(a)
    if ret > ms:
        ms = ret

    # Check BL-TR diagonals:
    ret = max_bltr_diagonals(a,n)
    if ret > ms:
        ms = ret

    # Check TL-BR diagonals:
    ret = max_tlbr_diagonals(a,n)
    if ret > ms:
        ms = ret

    if disp:
        print(ms)

    return ms

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

    def max_horizontal(a):
        """Generate all horizontal rows, and return max sum of any."""

        ms = 0
        for row in a:
            ret = max_sum(row)
            if ret > ms:
                ms = ret

        return ms

    def max_vertical(a):
        """Generate all vertical columns, and return max sum of any."""

        ms = 0
        for col in a.T:
            ret = max_sum(col)
            if ret > ms:
                ms = ret

        return ms

    def max_bltr_diagonals(a,n):
        """Generate all botton-left to top-right type lines, and return max sum of any."""

        ms = 0
        for j in range(n):
            diag = [ a[k,j-k] for k in range(j+1) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        for i in range(1,n):
            diag = [ a[k,i-k+n-1] for k in range(i,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        return ms

    def max_tlbr_diagonals(a,n):
        """Generate all top-left to bottom-right type lines, and return max sum of any."""

        ms = 0
        for i in range(n):
            diag = [ a[k,k-i] for k in range(i,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        for j in range(1,n):
            diag = [ a[k-j,k] for k in range(j,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        return ms


    # Check it works correctly:
    assert s(10) == -393027
    assert s(100) == 86613

    # Generate board:
    a = [ s(i) for i in range(1,n*n+1) ]
    a = np.array(a).reshape((n,n))
    ms = 0

    # Check horizontal rows:
    ms = max_horizontal(a)

    # Check vertical columns:
    ret = max_vertical(a)
    if ret > ms:
        ms = ret

    # Check BL-TR diagonals:
    ret = max_bltr_diagonals(a,n)
    if ret > ms:
        ms = ret

    # Check TL-BR diagonals:
    ret = max_tlbr_diagonals(a,n)
    if ret > ms:
        ms = ret

    if disp:
        print(ms)

    return ms

def f2(n, disp=True):
    """Generates an n*n square. n=2000 for original problem."""

    if disp:
        print("--- f2 ---")

    def max_sum(a):
        """Take list "a" and return largest sum of consecutive elements."""

        # "compact" to all-positive and all-negative "islands":
        compacted = [a[0]]

        for e in a[1:]:
            if e*compacted[-1] > 0: # equal sign
                compacted[-1] += e
            else:
                compacted.append(e)

        mx = -999999

        for i,ci in enumerate(compacted):
            if ci < 0:
                continue
            for j,cj in enumerate(compacted[i:]):
                if cj < 0:
                    continue
                v = sum(compacted[i:j+i+1])
                if v > mx:
                    mx = v

        return mx

    def max_horizontal(a):
        """Generate all horizontal rows, and return max sum of any."""

        ms = 0
        for row in a:
            ret = max_sum(row)
            if ret > ms:
                ms = ret

        return ms

    def max_vertical(a):
        """Generate all vertical columns, and return max sum of any."""

        ms = 0
        for col in a.T:
            ret = max_sum(col)
            if ret > ms:
                ms = ret

        return ms

    def max_bltr_diagonals(a,n):
        """Generate all botton-left to top-right type lines, and return max sum of any."""

        ms = 0
        for j in range(n):
            diag = [ a[k,j-k] for k in range(j+1) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        for i in range(1,n):
            diag = [ a[k,i-k+n-1] for k in range(i,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        return ms

    def max_tlbr_diagonals(a,n):
        """Generate all top-left to bottom-right type lines, and return max sum of any."""

        ms = 0
        for i in range(n):
            diag = [ a[k,k-i] for k in range(i,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        for j in range(1,n):
            diag = [ a[k-j,k] for k in range(j,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        return ms


    # Check it works correctly:
    assert s(10) == -393027
    assert s(100) == 86613

    # Generate board:
    a = [ s(i) for i in range(1,n*n+1) ]
    a = np.array(a).reshape((n,n))

    # Check horizontal rows (will be max so far):
    ms = max_horizontal(a)

    # Check vertical columns:
    ret = max_vertical(a)
    if ret > ms:
        ms = ret

    # Check BL-TR diagonals:
    ret = max_bltr_diagonals(a,n)
    if ret > ms:
        ms = ret

    # Check TL-BR diagonals:
    ret = max_tlbr_diagonals(a,n)
    if ret > ms:
        ms = ret

    if disp:
        print(ms)

    return ms

def f3(n, disp=True):
    """Generates an n*n square. n=2000 for original problem."""

    if disp:
        print("--- f3 ---")

    def max_sum(arr):
        """Take list "a" and return largest sum of consecutive elements."""

        # "compact" to all-positive and all-negative "islands":
        compacted = [arr[0]]

        for e in arr[1:]:
            if e*compacted[-1] > 0: # equal sign
                compacted[-1] += e
            else:
                compacted.append(e)

        # Remove first one, if negative, so we start from positive:
        if compacted[0] < 0:
            compacted = compacted[1:]

        mx = -999999

        m = len(compacted)
        for i in range(0,m,2):
            for j in range(i,m,2):
                s = sum(compacted[i:j+1])
                if s > mx:
                    mx = s

        return mx

    def max_horizontal(a):
        """Generate all horizontal rows, and return max sum of any."""

        ms = 0
        for row in a:
            ret = max_sum(row)
            if ret > ms:
                ms = ret

        return ms

    def max_vertical(a):
        """Generate all vertical columns, and return max sum of any."""

        ms = 0
        for col in a.T:
            ret = max_sum(col)
            if ret > ms:
                ms = ret

        return ms

    def max_bltr_diagonals(a,n):
        """Generate all botton-left to top-right type lines, and return max sum of any."""

        ms = 0
        for j in range(n):
            diag = [ a[k,j-k] for k in range(j+1) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        for i in range(1,n):
            diag = [ a[k,i-k+n-1] for k in range(i,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        return ms

    def max_tlbr_diagonals(a,n):
        """Generate all top-left to bottom-right type lines, and return max sum of any."""

        ms = 0
        for i in range(n):
            diag = [ a[k,k-i] for k in range(i,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        for j in range(1,n):
            diag = [ a[k-j,k] for k in range(j,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        return ms


    # Check it works correctly:
    assert s(10) == -393027
    assert s(100) == 86613

    # Generate board:
    a = [ s(i) for i in range(1,n*n+1) ]
    a = np.array(a).reshape((n,n))

    # Check horizontal rows (will be max so far):
    ms = max_horizontal(a)

    # Check vertical columns:
    ret = max_vertical(a)
    if ret > ms:
        ms = ret

    # Check BL-TR diagonals:
    ret = max_bltr_diagonals(a,n)
    if ret > ms:
        ms = ret

    # Check TL-BR diagonals:
    ret = max_tlbr_diagonals(a,n)
    if ret > ms:
        ms = ret

    if disp:
        print(ms)

    return ms

def f4(n, disp=True):
    """Generates an n*n square. n=2000 for original problem."""

    import numpy as np

    if disp:
        print("--- f4 ---")

    def max_sum(arr):
        """Take list "arr" and return largest sum of consecutive elements."""

        # "compact" to all-positive and all-negative "islands":
        compacted = [arr[0]]

        for e in arr[1:]:
            if e*compacted[-1] > 0: # equal sign
                compacted[-1] += e
            else:
                compacted.append(e)

        # Remove first one, if negative, so we start from positive:
        if compacted[0] < 0:
            compacted = compacted[1:]

        if not compacted: # then ALL were negative
            return 0

        mx = compacted[0]
        cum = mx
        m = len(compacted)

        for i in range(2,m,2):
            ci = compacted[i]
            cim1 = compacted[i-1]
            cum1 = cum + cim1
            if cum1 > 0:
                cum = cum1 + ci
            else:
                cum = ci
            mx = max(mx, cum, ci)

        mx = max(mx, cum)

        return mx

    def max_horizontal(a):
        """Generate all horizontal rows, and return max sum of any."""

        ms = 0
        for row in a:
            ret = max_sum(row)
            if ret > ms:
                ms = ret

        return ms

    def max_vertical(a):
        """Generate all vertical columns, and return max sum of any."""

        ms = 0
        for col in a.T:
            ret = max_sum(col)
            if ret > ms:
                ms = ret

        return ms

    def max_bltr_diagonals(a,n):
        """Generate all botton-left to top-right type lines, and return max sum of any."""

        ms = 0
        for j in range(n):
            diag = [ a[k,j-k] for k in range(j+1) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        for i in range(1,n):
            diag = [ a[k,i-k+n-1] for k in range(i,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        return ms

    def max_tlbr_diagonals(a,n):
        """Generate all top-left to bottom-right type lines, and return max sum of any."""

        ms = 0
        for i in range(n):
            diag = [ a[k,k-i] for k in range(i,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        for j in range(1,n):
            diag = [ a[k-j,k] for k in range(j,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        return ms


    # Check it works correctly:
    assert s(10) == -393027
    assert s(100) == 86613

    # Generate board:
    a = [ s(i) for i in range(1,n*n+1) ]
    a = np.array(a).reshape((n,n))

    # Check horizontal rows (will be max so far):
    ms = max_horizontal(a)

    # Check vertical columns:
    ret = max_vertical(a)
    if ret > ms:
        ms = ret

    # Check BL-TR diagonals:
    ret = max_bltr_diagonals(a,n)
    if ret > ms:
        ms = ret

    # Check TL-BR diagonals:
    ret = max_tlbr_diagonals(a,n)
    if ret > ms:
        ms = ret

    if disp:
        print(ms)

    return ms

def f5(n, disp=True):
    """Generates an n*n square. n=2000 for original problem."""

    if disp:
        print("--- f4 ---")

    def max_sum(arr):
        """Take list "arr" and return largest sum of consecutive elements."""

        # "compact" to all-positive and all-negative "islands":
        compacted = [arr[0]]

        for e in arr[1:]:
            if e*compacted[-1] > 0: # equal sign
                compacted[-1] += e
            else:
                compacted.append(e)

        # Remove first one, if negative, so we start from positive:
        if compacted[0] < 0:
            compacted = compacted[1:]

        if not compacted: # then ALL were negative
            return 0

        mx = compacted[0]
        cum = mx
        m = len(compacted)

        for i in range(2,m,2):
            ci = compacted[i]
            cim1 = compacted[i-1]
            cum1 = cum + cim1
            if cum1 > 0:
                cum = cum1 + ci
            else:
                cum = ci
            mx = max(mx, cum, ci)

        mx = max(mx, cum)

        return mx

    def max_horizontal(a):
        """Generate all horizontal rows, and return max sum of any."""

        ms = 0
        for row in a:
            ret = max_sum(row)
            if ret > ms:
                ms = ret

        return ms

    def max_vertical(a):
        """Generate all vertical columns, and return max sum of any."""

        return 0

        ms = 0
        for col in a.T:
            ret = max_sum(col)
            if ret > ms:
                ms = ret

        return ms

    def max_bltr_diagonals(a,n):
        """Generate all botton-left to top-right type lines, and return max sum of any."""

        ms = 0
        for j in range(n):
            #diag = [ a[k,j-k] for k in range(j+1) ]
            diag = [ a[k][j-k] for k in range(j+1) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        for i in range(1,n):
            #diag = [ a[k,i-k+n-1] for k in range(i,n) ]
            diag = [ a[k][i-k+n-1] for k in range(i,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        return ms

    def max_tlbr_diagonals(a,n):
        """Generate all top-left to bottom-right type lines, and return max sum of any."""

        ms = 0
        for i in range(n):
            #diag = [ a[k,k-i] for k in range(i,n) ]
            diag = [ a[k][k-i] for k in range(i,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        for j in range(1,n):
            #diag = [ a[k-j,k] for k in range(j,n) ]
            diag = [ a[k-j][k] for k in range(j,n) ]
            ret = max_sum(diag)
            if ret > ms:
                ms = ret

        return ms


    # Check it works correctly:
    assert s(10) == -393027
    assert s(100) == 86613

    # Generate board:
    #a = [ s(i) for i in range(1,n*n+1) ]
    #a = np.array(a).reshape((n,n))
    a = []
    for i in range(n):
        a.append([])
        for j in range(n):
            ij = i*n + j + 1
            a[i].append(s(ij))

    # Check horizontal rows (will be max so far):
    ms = max_horizontal(a)

    # Check vertical columns:
    ret = max_vertical(a)
    if ret > ms:
        ms = ret

    # Check BL-TR diagonals:
    ret = max_bltr_diagonals(a,n)
    if ret > ms:
        ms = ret

    # Check TL-BR diagonals:
    ret = max_tlbr_diagonals(a,n)
    if ret > ms:
        ms = ret

    if disp:
        print(ms)

    return ms


#------------------------------------------------------------------------------#

if __name__ == "__main__":
    times = []
    for i in [4]:
        t = timeit.Timer('f{0}(2000)'.format(i), "from __main__ import f{0}".format(i))
        times.append([i, t.timeit(number=1)])

    # Python 3.x times #

    #    n    res(n)  function  time (ms)
    #  100   8642499        f0      ~1600
    #                       f1      ~1100
    #                       f2       ~150
    #                       f3       ~130
    #                       f4        ~19
    #
    #  200  11614980        f0     ~21000
    #                       f1     ~14000
    #                       f2      ~1600
    #                       f3      ~1450
    #                       f4        ~75
    #
    #  400  19187069        f2     ~22000
    #                       f3     ~21000
    #                       f4       ~315
    #
    #  800  29743196        f2    ~305000
    #                       f3    ~290000
    #                       f4      ~1700
    #
    # 1200  39294806        f4      ~3900
    #
    # 2000  52852124        f4     ~10500

    print("\nTimes:\n")
    for i,t in times:
        if t < 2:
            print('t(f{i}) = {t:.1f} ms'.format(i=i, t=t*1000))
        else:
            print('t(f{i}) = {t:.1f} s'.format(i=i, t=t))
