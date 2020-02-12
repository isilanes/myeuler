from libeuler import core


class p152(core.FunctionSet):

    def f0(self, n):

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
                s.append(t - 524288)  # 2**19 = 524288

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
        for i in range(n):
            for j in range(i+1):
                for k in range(n-i):
                    ret = subt(triang,i,j,k)
                    if ret < ms:
                        ms = ret

        return ms

    def f1(self, n):
        """Same as f0, with memoization.
        Works, but uses INSANE amounts of memory, plus still too slow."""

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
        for i in range(n):
            for j in range(i+1):
                for k in range(n-i):
                    ret = subt(triang,i,j,k)
                    if ret < ms:
                        ms = ret

        return ms

    def f2(self, n):
        """Take f1 and avoid memoization, in lieu of doing things in the proper order."""

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
        for i in range(n):
            for j in range(i+1):
                ts = 0
                for k in range(i,n):
                    ts += sum(triang[k][j:j+k-i+1])
                    if ts < ms:
                        ms = ts

        return ms

    def f3(self, n):
        """Take f2, and precalculate line sums:."""


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

        # Build triangle:
        s = build_s(n)

        k = 0
        triang = []
        for i in range(n):
            triang.append([])
            for j in range(i+1):
                triang[-1].append(s[k])
                k += 1

        # Build line-sum triangle:
        striang = []
        for i in range(n):
            acc = 0
            line = []
            for j in range(i+1):
                acc += triang[i][j]
                line.append(acc)
            striang.append(line)

        # Find the sums of all subtriangles:
        ms = 0
        for i in range(n):
            for j in range(i+1):
                ts = 0
                for k in range(i,n):
                    ts += striang[k][j+k-i] - striang[k][j-1]
                    if ts < ms:
                        ms = ts

        return ms


P = p152()
P.run()

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

# PyPy @ Python @ GCC times (Burns)
#
#    n     res(n)  function  time (ms)
#
#  200  -87957828        f0      24400
#                        f1       3100

# Python 3.5.2 times (Skinner)
#
#    n      res(n)  function  time (ms)
#
#    2     -153582        f0        0.2
#                         f1        0.1
#                         f2        0.1
#                         f3        0.2
#
#   10    -1495491        f0        0.4
#                         f1        0.3
#                         f2        0.2
#                         f3        0.3
#
#  100   -38951741        f0       2700
#                         f1        250
#                         f2        117
#                         f3         32
#
#  200   -87957828        f0      62000
#                         f1       2300
#                         f2       1400
#                         f3        240
#
#  400  -185446601        f1      25400
#                         f2      17700
#                         f3       2300
#
#  600  -214798728        f2      86200
#                         f3       8600
#
# 1000  -271248680        f3      41800

# PyPy 5.1.2 @ Python 2.7.10 @ GCC 5.3.1 times (Skinner)
#
#    n      res(n)  function  time (ms)
#
#  200   -87957828        f0       9100
#                         f1       1200
#                         f2        195
#                         f3         16
#
#  400  -185446601        f1       9500
#                         f2       2200
#                         f3         77
#
#  600  -214798728        f2      10200
#                         f3        635
#
# 1000  -271248680        f2      74700
#                         f3       3100
