#--------------------------------------------------------------------#

def f0(N):
    print("--- f0 ---")

    def next(N):
        '''
        Square digits in N, add squares up, and return result.
        '''

        digs = [ int(x)**2 for x in str(N) ]
        return sum(digs)

    res = 0
    for i in range(2,N+1):
        n = next(i)
        while True:
            if n == 89:
                res += 1
                break
            if n == 1:
                break
            n = next(n)

    print(res)

#--------------------------------------------------------------------#

def f1(N):
    print("--- f1 ---")

    def ends_in_89(N):
        '''
        Return True if the sequence starting at N ends in 89, 
        False otherwise (because it ends in 1).
        '''

        if N == 89:
            return True

        if N == 1:
            return False

        return ends_in_89(next(N))

    def next(N):
        '''
        Square digits in N, add squares up, and return result.
        '''

        digs = [ int(x)**2 for x in str(N) ]
        return sum(digs)

    class Memoize(object):

        def __init__(self, fun):
            self.fun = fun
            self.cache = {}

        def __call__(self, *args):
            if not args in self.cache:
                self.cache[args] = self.fun(*args)
            return self.cache[args]

    ends_in_89 = Memoize(ends_in_89)

    res = 0
    for i in range(2,N+1):
        if ends_in_89(i):
            res += 1

    print(res)

#--------------------------------------------------------------------#

def f2(N):
    print("--- f2 ---")

    def next(N):
        '''
        Square digits in N, add squares up, and return result.
        '''

        digs = [ int(x)**2 for x in str(N) ]
        return sum(digs)

    res = 0
    endsin = {}
    for i in range(2,N+1):
        if i in endsin:
            if endsin[i] == 89:
                res += 1
                continue

        chain = [i]
        n = next(i)
        while True:
            chain.append(n)

            if n in endsin:
                end = endsin[n]
                break
            if n == 1:
                end = 1
                break
            if n == 89:
                end = 89
                break
            n = next(n)

        if end == 89:
            res += 1

        for slab in chain:
            endsin[slab] = end

    print(res)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(3):
    t = timeit.Timer('f{0}(10*1000*1000)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 55 s (pypy)
# f1: ~ 44 s (pypy)
# f2: ~ 16 s (pypy) - slow at first, scales better so better at high N
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
