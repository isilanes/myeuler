#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def combos(N):
        '''
        Return the amount of combos for a total length of N tiles.
        '''

        if N == 3:
            return 2
        if N < 3:
            return 1
        tot = 1
        for n in range(3,N+1):
            for begin in range(N-n+1):
                tot += combos(N-begin-n-1)
        return tot

    print(combos(50))

#--------------------------------------------------------------------#

def f1():
    '''
    Same as f0, with memoization.
    '''
    print("--- f1 ---")

    class Memoize(object):

        def __init__(self, fun):
            self.fun = fun
            self.cache = {}

        def __call__(self, *args):
            if not args in self.cache:
                self.cache[args] = self.fun(*args)
            return self.cache[args]

    def combos(N):
        '''
        Return the amount of combos for a total length of N tiles.
        '''

        if N == 3:
            return 2
        if N < 3:
            return 1
        tot = 1
        for n in range(3,N+1):
            for begin in range(N-n+1):
                tot += combos(N-begin-n-1)
        return tot

    combos = Memoize(combos)
    print(combos(50))

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(2):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: too slow (~ 1150s pypy)
# f1: ~ 13 ms (python2)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
