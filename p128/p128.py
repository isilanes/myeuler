def f0(nth):
    print("--- f0 ---")

    def isprime(num):
        '''Returns True if num is prime, False otherwise.'''

        if num == 1:
            return False

        if num in [2,3,5,7]:
            return True

        if num % 10 in [0,2,4,5,6,8]:
            return False

        i = 3
        while i*i < num+1:
            if not num % i:
                return False
            i += 2

        return True
        
    def isZ1(n):
        # 3 possible prime differences in single Z1 cell of ring n:
        D2 = 6*n + 1
        D3 = 6*n - 1
        D6 = 6*(2*n+1) - 1

        # All three must be prime. If any is not, quit early:
        if isprime(D2) and isprime(D3) and isprime(D6):
            return True
        return False

    def isZ13(n):
        # 3 possible prime differences in single Z13 cell of ring n:
        D2 = 6*n - 1
        D3 = 6*(2*n - 1) - 1
        D6 = 6*(n + 1) - 1

        if isprime(D2) and isprime(D3) and isprime(D6):
            return True
        return False

    def Z1(n):
        return 3*(n**2-n) + 2

    def Z13(n):
        return 3*(n**2+n) + 1


    # See README.

    # 0th ring:
    npd3 = 1 # i = 1

    # 1st ring:
    npd3 += 1 # i = 2

    # From ring n=2 on:
    n = 2
    while True:
        if isZ1(n):
            npd3 += 1
            if npd3 == nth:
                print npd3, Z1(n)
                break
        if isZ13(n):
            npd3 += 1
            if npd3 == nth:
                print npd3, Z13(n)
                break
        n += 1
        

#------------------------------------------------------------------------------#

import timeit

times = []
for i in [0]:
    t = timeit.Timer('f{0}(2000)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~2.7 s (python), ~640 ms (pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
