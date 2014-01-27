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

    def combos(N):
        '''
        Return the amount of combos for L-length tiles inside a 
        total length of N tiles, where L is within "lengths".
        '''

        tiles = [2,3,4]

        if N == tiles[0]:
            return 1
        if N < tiles[0]:
            return 0
        tot = 0
        for L in tiles:
            for begin in range(N-L+1):
                tot += combos(N-begin-L) + 1
        return tot

    combos = Memoize(combos)
    tot = combos(50) + 1 # +1 for the all-black solution
    print(tot)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 3 ms (python2)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
