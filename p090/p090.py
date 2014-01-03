#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import itertools as it

    def are_valid(cA, cB, sq):
        '''
        Return whether combos cA and cB allow for creation of all
        squares from 01 to 81.
        '''

        for a,b in sq:
            if a in cA and b in cB:
                continue
            elif b in cA and a in cB:
                continue
            else:
                return False

        return True

    # Square list:
    sq = []
    for i in range(1,10):
        s = '{0:02d}'.format(i*i)
        s = (int(s[0]), int(s[1]))
        sq.append(s)

    # Generate all possible combos.
    combos = {}
    
    for combo in it.combinations(range(10), 6):
        if 6 in combo and not 9 in combo:
            combo += (9,)
        elif 9 in combo and not 6 in combo:
            combo += (6,)
        combos[combo] = True

    combos = combos.keys()

    # Loop over and count:
    res = 0
    n = len(combos)
    for i in range(n):
        comboi = combos[i]
        for j in range(i):
            comboj = combos[j]
            if are_valid(comboi, comboj, sq):
                res += 1

    print(res)
    
#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: 24 ms (python2)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
