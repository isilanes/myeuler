#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    ndigits = 100

    # --- Increasings numbers --- #

    # Digits go from 1st to 100th. For increasing
    # numbers ith digit must be equal to or higher than
    # (i-1)th digit.

    # When 99th digit is i, sum of all possible 100th
    # digit cases is s[i]:
    s = [ 10 - x for x in range(10) ]

    # There are 98 previous digits for which the process
    # must be repeated:
    for j in range(ndigits-2):
        for i in range(10):
            s[i] = sum(s[i:])

    # Do not count zero (subtract one):
    nincreasing = sum(s) - 1

    # --- Decreasing numbers --- #

    # Recall numbers with M leading zeros can still be decreasing
    # numbers (even if (M+1)th digit is larger than zero (Mth),
    # because they are actually (100-M)-digit numbers. So to find
    # out the amount of decreasing numbers we must do otherwise.

    # For 1 digit:
    ndecreasing = 9 # 10 minus the zero

    # For 2 digits:
    s = [ x for x in range(1,11) ]
    ndecreasing += sum(s) - 1 # minus the zero

    # For 3+ digits:
    for j in range(2,ndigits):
        for i in range(9,-1,-1):
            s[i] = sum(s[:i+1])
        ndecreasing += sum(s) - 1 # minus the zero

    # Amount of non-bouncy numbers is amount of increasing plus
    # amount of decreasing (plus reduntands, see below):
    nonbouncy = nincreasing + ndecreasing

    # All j-digit numbers, j=1 to j=ndigits, in which all digits 
    # are equal have been counted twice (remove them once):
    nonbouncy -= ndigits*9

    # Result:
    print(nonbouncy)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 1.1 ms (python2)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
