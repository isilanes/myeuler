#--------------------------------------------------------------------#

def f0(N):
    print("--- f0 ---")

    import itertools as it

    def is_special(S):
        '''
        Return True if S is a valid special set.
        '''

        n = len(S) // 2
        # All subset pairs:
        for size in range(n,0,-1):
            for combo in it.combinations(S, size):
                rem = list(S)
                for e in combo:
                    rem.remove(e)
                for i in range(size,len(rem)+1):
                    for other in it.combinations(rem, i):
                        if sum(combo) > sum(other):
                            if len(combo) < len(other):
                                return False
                        elif sum(combo) == sum(other):
                            return False
                        elif len(combo) > len(other):
                            return False

        return True

    special = [1]
    for n in range(2,N+1):
        j = len(special) // 2
        b = special[j]
        guess = [b] + [ x + b for x in special ]
        max_sum = sum(guess)
        kmax = max_sum - (n-1)*b - (n-1)*(n-2)/2
        best = guess
        for combo in it.combinations(range(b+1,kmax+1), n-1):
            guess = [b] + [ x for x in combo ]
            if sum(guess) < max_sum and is_special(guess):
                best = guess
                max_sum = sum(best)
        print n, best, ''.join([ str(x) for x  in best ])
        special = best

#--------------------------------------------------------------------#

def f1(N):
    print("--- f1 ---")

    import itertools as it

    def is_special(S):
        '''
        Return True if S is a valid special set.
        '''

        # Check that 1..n-1 last elements add up to more than 2..n 
        # elements combined. If not, exit early.
        S.sort()
        n = len(S) // 2
        for i in range(1,n+1):
            if sum(S[-i:]) >= sum(S[:i+1]):
                return False

        # It only remains to check that no two equal-length subsets
        # add up to the same amount:
        for i in range(2,n+1):
            dict = {}
            for combo in it.combinations(S,i):
                s = sum(combo)
                if s in dict:
                    return False
                else:
                    dict[s] = True

        return True
    
    special = [1]
    for n in range(2,N+1):
        j = len(special) // 2
        b = special[j]
        guess = [b] + [ x + b for x in special ]
        max_sum = sum(guess)
        kmax = max_sum - (n-1)*b - (n-1)*(n-2)/2
        best = guess
        for combo in it.combinations(range(b+1,kmax+1), n-1):
            guess = [b] + [ x for x in combo ]
            if sum(guess) < max_sum and is_special(guess):
                best = guess
                max_sum = sum(best)
        print n, best, ''.join([ str(x) for x  in best ])
        special = best

#--------------------------------------------------------------------#

def f2(N):
    print("--- f2 ---")

    import itertools as it

    def is_special(S):
        '''
        Return True if S is a valid special set.
        '''

        # Check that 1..n-1 last elements add up to more than 2..n 
        # elements combined. If not, exit early.
        S.sort()
        n = len(S) // 2
        for i in range(1,n+1):
            if sum(S[-i:]) >= sum(S[:i+1]):
                return False

        # It only remains to check that no two equal-length subsets
        # add up to the same amount:
        for i in range(2,n+1):
            dict = {}
            for combo in it.combinations(S,i):
                s = sum(combo)
                if s in dict:
                    return False
                else:
                    dict[s] = True
                
        return True

    def all_adding(N, n, imin):
        '''
        Return all combinations of n different numbers i, such
        that they add up to N, and where the smallest i is equal to
        or larger than imin.
        '''

        if N < n or N < imin:
            return [[]]
        if n == 1:
            return [[N]]
        else:
            # imax: if 1..n-1 are minimal, and nth maximal
            imax = N - imin*(n-1) - (n-1)*(n-2)/2
            res = []
            for i in range(imin, imax+1):
                new_N = N - i
                new_n = n - 1
                new_imin = i + 1
                for new in all_adding(new_N, new_n, new_imin):
                    if len(new) == n - 1:
                        res.append([i] + new)
            return res

    def loop(s, n, b):
        for c in all_adding(s, n-1, b+1):
            if len(c) == n - 1:
                g = [b] + c
                if is_special(g):
                    return g

        return None

    special = [1]
    for n in range(2,N+1):
        j = len(special) // 2
        b = special[j]
        guess = [b] + [ x + b for x in special ]
        smax = sum(guess) - b
        smin = b*(n-1) + n*(n-1)/2

        # Check all s from smin to smax. For each s, find all 
        # combinations of n-1 different numbers (greater than b) that
        # add up to s, and check if they are a special set. If we check
        # s values increasingly, the first match will be our answer.
        best = guess
        for s in range(smin, smax+1):
            res = loop(s, n, b)
            if res:
                best = res
                break

        print n, best, ''.join([ str(x) for x  in best ])
        special = best

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(3):
    t = timeit.Timer('f{0}(7)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: too slow    (~ 860 s, pypy)
# f1: too slow    (~ 700 s, pypy)
# f2: fast enough (~   8 s, pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
