#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    # --- Increasings numbers --- #

    # Digits go from 1st to 100th. For increasing
    # numbers ith digit must be equal to or higher than
    # (i-1)th digit.

    # When 99th digit is i, sum of all possible 100th
    # digit cases is s[i]:
    s = [ 10 - x for x in range(10) ]

    # There are 98 previous digits for which the process
    # must be repeated:
    for j in range(4):
        for i in range(10):
            s[i] = sum(s[i:])

    nincreasing = sum(s)
    nincreasing -= 1 # do not count zero as "increasing" (or anything)

    print nincreasing

    # --- Decreasing numbers --- #

    # Recall numbers with M leading zeros can still be decreasing
    # numbers (even if (M+1)th digit is larger than zero (Mth),
    # because they are actually (100-M)-digit numbers. So to find
    # out the amount of decreasing numbers we must do otherwise.
    for ndigs in range(2,101):
        pass

    # Also, in general, all N-digit numbers, N=1 to 100, in
    # which all digits are equal have been counted twice:
    nonbouncy -= 6*9

    print(nonbouncy)

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
