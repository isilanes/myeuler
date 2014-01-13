#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    un = []
    for n in range(10):
        x = 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8\
                - n**9 + n**10
        print n, x

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: too slow (~ 1400 s for 10**9 with pypy)
# f1: too slow (~ 5400 s for 10**9 with pypy)
# f2: too slow (~  895 s for 10**9 with pypy)
# f3: ~ 1.3 s (pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
