#--------------------------------------------------------------------#

def f0(N):
    print("--- f0 ---")

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

    res = 0
    with open("sets.txt") as f:
        for line in f:
            S = [ int(x) for x in line.split(',') ]
            if is_special(S):
                res += sum(S)

    print(res)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}(7)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 12 ms (python3)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
