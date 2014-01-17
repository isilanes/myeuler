#--------------------------------------------------------------------#

def f0(N):
    print("--- f0 ---")

    import itertools as it

    def unclear(c):
        '''
        Take combo "c", and assume it's the half of S = range(2*len(c)).
        Then, return False if the sum of ith elemts for i in c would be 
        clearly higher than that of other half of S, K (S = c + K),
        True if unclear.
        '''

        for i in range(len(c)):
            # i-th element in c will have c[i] elements of S
            # and i elements of c below itself. That is, it will
            # have c[i] - i elements of K below itself. i-th element 
            # of c must have i+1 elements of K below itself for it 
            # to be a clear win of c over K.
            below = c[i] - i
            if below < i+1:
                return True

        return False
    
    def unclear_combos(P):
        '''
        Given a set S with len(S) = 2*P, and taking all combos of
        two disjoint P-length subsets, how many of them have no 
        clear sum-winner.
        '''

        n = 0
        for combo in it.combinations(range(2*P-1), P-1):
            c = combo + (2*P-1,)
            if unclear(c):
                n += 1

        return n

    def fac(N):
        '''
        Return N!
        '''
        if N < 2:
            return 1
        else:
            return N*fac(N-1)

    def cmn(N,M):
        '''
        Return N choose M.
        '''

        return fac(N) / (fac(M)*fac(N-M))

    N = 12
    tot = 0
    maxP = N // 2
    for P in range(2,maxP+1):
        n = unclear_combos(P) * cmn(N,2*P)
        tot += n
    print(tot)

#--------------------------------------------------------------------#

def f1(N):
    print("--- f1 ---")

    import itertools as it

    def unclear(c):
        '''
        Take combo "c", and assume it's the half of S = range(2*len(c)).
        Then, return False if the sum of ith elemts for i in c would be 
        clearly higher than that of other half of S, K (S = c + K),
        True if unclear.
        '''

        for i in range(len(c)):
            # i-th element in c will have c[i] elements of S
            # and i elements of c below itself. That is, it will
            # have c[i] - i elements of K below itself. i-th element 
            # of c must have i+1 elements of K below itself for it 
            # to be a clear win of c over K.
            below = c[i] - i
            if below < i+1:
                return True

        return False
    
    def unclear_combos(P):
        '''
        Given a set S with len(S) = 2*P, and taking all combos of
        two disjoint P-length subsets, how many of them have no 
        clear sum-winner.
        '''

        n = 0
        for combo in it.combinations(range(2*P-1), P-1):
            c = combo + (2*P-1,)
            if unclear(c):
                n += 1

        return n

    def cmn(N,M):
        '''Return N choose M.'''
        return facs[N] / (facs[M]*facs[N-M])

    N = 12

    # Precalculate all factorials:
    facs = [1]
    f = 1
    for i in range(1,N+1):
        f = f * i
        facs.append(f)

    tot = 0
    maxP = N // 2
    for P in range(2,maxP+1):
        n = unclear_combos(P) * cmn(N,2*P)
        tot += n
    print(tot)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(2):
    t = timeit.Timer('f{0}(7)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 0.9 ms (python)
# f1: ~ 0.8 ms (python)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
