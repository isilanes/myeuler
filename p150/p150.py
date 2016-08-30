# -*- coding=utf-8 -*-

import timeit

def f5(n, disp=True):

    if disp:
        print("--- f5 ---")

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

    def max_vertical(a,n):
        """Generate all vertical columns, and return max sum of any."""

        ms = 0
        for j in range(n):
            col = [ a[i][j] for i in range(n) ]
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
    ret = max_vertical(a,n)
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

def f0(n, disp=True):

    if disp:
        print("--- f0 ---")

    def memoize(f):
        cache = {}
        def helper(x):
            if x not in cache:
                cache[x] = f(x)

            return cache[x]


        return helper

    @memoize
    def s(k):
        return [15, -14, -7, 20, -13, -5, -3, 8, 23, -26, 1, -4, -5, -18, 5, -16, 31, 2, 9, 28, 3][k]

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

    def subt(triang,i,j,k):
        if k == 0:
            return triang[i][j]
        else:
            return subt(triang,i,j,k-1) + sum(triang[i+k][j:j+k+1])


    # Build triangle:
    k = 0
    triang = []
    for i in range(n):
        triang.append([])
        for j in range(i+1):
            triang[-1].append(s(k))
            k += 1

    # Find the sums of all subtriangles:
    ms = 0
    for i in range(n):
        for j in range(i+1):
            for k in range(n-i):
                ret = subt(triang,i,j,k)
                if ret < ms:
                    ms = ret

    if disp:
        print(ms)

    return ms


#------------------------------------------------------------------------------#

if __name__ == "__main__":
    times = []
    for i in [0]:
        t = timeit.Timer('f{0}(6)'.format(i), "from __main__ import f{0}".format(i))
        times.append([i, t.timeit(number=1)])

    # Python 3.5.2 times
    #
    #    n    res(n)  function  time (ms)
    #  100   8642499        f0      ~1200
    #                       f1      ~1150

    # PyPy 5.1.1 @ Python 2.7.10 times
    #
    # 2000  52852124        f5       ~950

    print("\nTimes:\n")
    for i,t in times:
        if t < 2:
            print('t(f{i}) = {t:.1f} ms'.format(i=i, t=t*1000))
        else:
            print('t(f{i}) = {t:.1f} s'.format(i=i, t=t))
