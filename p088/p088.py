#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import itertools as it

    def factors(N):
        '''
        Return factors of N.
        '''

        facs = []
        for i in range(2,N+1):
            while not N % i:
                facs.append(i)
                N = N / i
            if N == 1:
                break
            i += 1
        
        return facs

    def ways(N):
        '''
        Return a list of arrays, each containing M integers, such that
        the product of all integers within each array gives N. The arrays
        represent *ALL* possible ways of getting N through products of integers.
        '''

        facs = factors(N)
        nf = len(facs)
        if nf == 1:
            return ((N,),)
        
        w = ()
        for i in range(1,nf):
            combos = set(it.combinations(facs, i))
            for combo in combos:
                p = 1
                for c in combo:
                    p = p * c
                res = N / p
                w = w + ((p, res),)
                for way in ways(res):
                    w = w + ((p,) + way,)
                    
        w = [ tuple(sorted(x)) for x in w ]
        return set(w)
    
    # We will go up to this k:
    k_lim = 12*1000
    
    # Dictionary of k -> N, where k = length of product-summation,
    # and N = lowest number with that k:
    D = {}
    for k in range(2,k_lim+1):
        D[k] = 999999
    
    # Loop over Ns, until we fully populate D:
    N = 4
    while 999999 in D.values():
        for way in ways(N):
            if len(way) > 1:
                s = sum(way)
                o = N - s # extra 1s
                k = len(way) + o # number of elements
                try:
                    D[k] = min(N,D[k])
                except:
                    D[k] = N
        N += 1
    
    inver = {}
    for k in sorted(D.keys())[:k_lim-1]:
        inver[D[k]] = k
    
    print(sum(inver.keys()))

#--------------------------------------------------------------------#

def f1():
    print("--- f1 ---")

    import itertools as it

    def factors(N):
        '''
        Return factors of N.
        '''

        facs = []
        for i in range(2,N+1):
            while not N % i:
                facs.append(i)
                N = N / i
            if N == 1:
                break
            i += 1
        
        return facs

    def ways(N):
        '''
        Return a list of arrays, each containing M integers, such that
        the product of all integers within each array gives N. The arrays
        represent *ALL* possible ways of getting N through products of integers.
        '''

        facs = factors(N)
        nf = len(facs)
        if nf == 1:
            return ((N,),)
        
        w = ()
        for i in range(1,nf):
            combos = set(it.combinations(facs, i))
            for combo in combos:
                p = 1
                for c in combo:
                    p = p * c
                res = N / p
                w = w + ((p, res),)
                for way in ways(res):
                    w = w + ((p,) + way,)
                    
        w = [ tuple(sorted(x)) for x in w ]
        return set(w)
    
    class Memoize(object):

        def __init__(self, fun):
            self.fun = fun
            self.cache = {}

        def __call__(self, *args):
            if not args in self.cache:
                self.cache[args] = self.fun(*args)
            return self.cache[args]
    
    ways = Memoize(ways)

    # We will go up to this k:
    k_lim = 12*1000
    
    # Dictionary of k -> N, where k = length of product-summation,
    # and N = lowest number with that k:
    D = {}
    for k in range(2,k_lim+1):
        D[k] = 999999
    
    # Loop over Ns, until we fully populate D:
    N = 4
    while 999999 in D.values():
        for way in ways(N):
            if len(way) > 1:
                s = sum(way)
                o = N - s # extra 1s
                k = len(way) + o # number of elements
                try:
                    D[k] = min(N,D[k])
                except:
                    D[k] = N
        N += 1
    
    inver = {}
    for k in sorted(D.keys())[:k_lim-1]:
        inver[D[k]] = k
    
    print(sum(inver.keys()))

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(2):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 22 s
# f1: ~ 4.3 s
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
