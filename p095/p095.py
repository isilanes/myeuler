#--------------------------------------------------------------------#

def f0(max):
    print("--- f0 ---")

    # Find proper divisors of all numbers up to max, using a sieve:
    propers = {}
    for i in range(1,max+1):
        p = i*2
        while p < max+1:
            try:
                propers[p].append(i)
            except:
                propers[p] = [i]
            p += i

    def next(N, propers):
        '''
        Return sum of proper divisors of N, potentially the next
        element in a amicable chain.
        '''

        return sum(propers[N])

    n = 10
    for i in range(10):
        m = next(n, propers)
        print n, m
        if m == 1:
            break
        n = m

    '''
    for i in range(2,max+1):
        chain = [i]
        n = next(i, propers)
        if i == next(i, propers):
            print(i)
    '''

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}(100)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 270 s
# f1: ~ 291 s (even slower!)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
