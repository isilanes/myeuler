#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    class Memoize(object):

        def __init__(self, fun):
            self.fun = fun
            self.cache = {}

        def __call__(self, *args):
            if not args in self.cache:
                self.cache[args] = self.fun(*args)
            return self.cache[args]

    def combos(N,L):
        '''
        Return the amount of combos for L-length tiles inside a 
        total length of N tiles.
        '''

        if N == L:
            return 1
        if N < L:
            return 0
        tot = 0
        for begin in range(N-L+1):
            tot += combos(N-begin-L,L) + 1
        return tot

    def red_combos(N):
        '''
        Return the amount of combos for red tiles inside a total 
        length of N tiles.
        '''

        return combos(N,2)

    def green_combos(N):
        '''
        Return the amount of combos for green tiles inside a total 
        length of N tiles.
        '''

        return combos(N,3)

    def blue_combos(N):
        '''
        Return the amount of combos for blue tiles inside a total 
        length of N tiles.
        '''

        return combos(N,4)

    combos = Memoize(combos)
    N = 50
    tot = red_combos(N) + green_combos(N) + blue_combos(N)

    print(tot)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 2.4 ms (python2)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
