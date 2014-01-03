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
        #s = s.replace('9','6')
        s = (int(s[0]), int(s[1]))
        sq.append(s)

    # Combos:
    combosA = [ x for x in it.combinations(range(10), 6) ]
    combosB = [ x for x in it.combinations(range(10), 6) ]
    for comboA in combosA:
        for comboB in combosB:
            if are_valid(comboA, comboB, sq):
                print comboA, comboB
    
#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: 8 ms (python2)
# f1: 0.8 ms (python2)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
