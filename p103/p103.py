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
        for i in range(1,n):
            if sum(S[-i:]) <= sum(S[:i+1]):
                return False

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
                                #return False
                                pass
                        if sum(combo) == sum(other):
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

import timeit

times = []
for i in range(2):
    t = timeit.Timer('f{0}(5)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: too slow (~ 850 s)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
