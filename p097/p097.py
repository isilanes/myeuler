#--------------------------------------------------------------------#

def f0(max):
    print("--- f0 ---")
    
    a = 28433*2**max + 1
    print str(a)[-10:]

#--------------------------------------------------------------------#

def f1(max):
    print("--- f1 ---")

    # max = N in p = 28433*2**N + 1 (so max = 7830457).

    # To get last N digits of 2**n, start with 2 and multiply times 2
    # (n - 1) times, keeping each time only last N digits. Digits
    # prior to last N will never change the last N digits after 
    # multiplication times 2 (or any integer).
    tmp = 2
    for step in range(max-1):
        tmp = tmp * 2
        tmp = str(tmp)[-10:]
        tmp = int(tmp)

    tmp = 28433*tmp + 1
    print(str(tmp)[-10:])

#--------------------------------------------------------------------#

def f2(max):
    print("--- f2 ---")

    res = (28433*2**max + 1) % 10**10
    print(res)

#--------------------------------------------------------------------#

def f3(max):
    print("--- f3 ---")

    res = (pow(2, 7830457, 10**10) * 28433 + 1) % 10**10
    print(res)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1,4):
    t = timeit.Timer('f{0}(7830457)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 385 s (pypy)
# f1: ~ 2.4 s (pypy)
# f2: ~ 6.8 ms (pypy)
# f3: ~ 0.08 ms (python)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
