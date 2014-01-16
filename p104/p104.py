#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    check = '123456789'

    n = 2 # n of current F(n)
    fib = 1 # F(n) for current n
    fib_old = 1 # F(n-1) for current n
    while True:
        n += 1
        fib_old, fib = fib, fib + fib_old

        # Last 9 digits:
        tail = [ x for x in str(fib % 1000000000) ]
        tail.sort()
        tail = ''.join(tail)

        if tail == check:
            s = str(fib)
            # First 9 digits:
            head = [ x for x in s[:9] ]
            head.sort()
            head = ''.join(head)
            if head == check:
                print(n)
                break

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 30 s (python)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
