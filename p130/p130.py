import timeit

#------------------------------------------------------------------------------#

def f0(ncomp):
    print("--- f0 ---")

    def A(n):
        '''Returns A(n) for n.'''

        k = 1
        rem = 1
        while True:
            rem = (rem + pow(10, k, n)) % n
            if not rem:
                return k + 1
            k += 1

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


    comps = []
    p = 89
    while len(comps) < ncomp:
        p += 2
        if p % 5 and not isprime(p):
            a = A(p)
            if not (p - 1) % a:
                comps.append(p)
    
    print(sum(comps))


#------------------------------------------------------------------------------#

times = []
for i in [0]:
    t = timeit.Timer('f{0}(25)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

# pypy times

# f0:    ncomp  t (ms)
#            5      12
#           15     596
#           25    3005

print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
