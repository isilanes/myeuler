#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    import itertools as it

    tot = 0
    for combo in it.permutations([1,2,3,4,5,6,7,8,9], 9):
        tot += 1

    print(tot)

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
