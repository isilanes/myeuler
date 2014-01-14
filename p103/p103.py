#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import itertools as it

    def is_special(S):
        '''
        Return True if S is a valid special set.
        '''

        n = len(S) // 2
        # All subset pairs:
        for size in range(1,n+1):
            for combo in it.combinations(S, size):
                other = S[:]
                for e in combo:
                    other.remove(e)
                if sum(combo) == sum(other):
                    return False
                if sum(combo) > sum(other):
                    if len(combo) < len(other):
                        return False
                else:
                    if len(combo) > len(other):
                        return False

        return True

    special = [1]
    n = 1
    for i in range(10):
        j = len(special) // 2
        b = special[j]
        n += 1
        guess = [b] + [ x + b for x in special ]
        max_sum = sum(guess)
        print max_sum, n

        break

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0:
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
