#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def is_palindromic(n):
        s = str(n)
        return s == s[::-1]

    # List of all squares up to 10**8:
    sq = [ x*x for x in range(1,10**4+1) ]

    # Get N = 2, 3... consecutive squares, add them up, and add to
    # result if palindromic:
    res = []
    for N in range(2,10**8):
        sq0 = sq[:N]
        if sum(sq0) > 10**8:
            break
        for i in range(10**4+1-N):
            sqs = sq[i:i+N]
            n = sum(sqs)
            if n > 10**8:
                break
            if is_palindromic(n):
                res.append(n)

    print(sum(set(res)))

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 5.8 s (python)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
