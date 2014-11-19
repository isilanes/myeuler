import math
import timeit

#------------------------------------------------------------------------------#

def f0(maxn):
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


    for num in range(10,10**5):
        isprime(num**2+1)


#------------------------------------------------------------------------------#

times = []
for i in [0]:
    t = timeit.Timer('f{0}(10**3)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:  maxp1  t (ms)

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
