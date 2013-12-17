#--------------------------------------------------------------------#

def f0():
    print("--- f0 ---")

    def factors_of(num):
        '''
        Return the factors of number n.
        '''
        factors = []
        for i in range(2,num/2+1):
            if not num % i:
                factors.append(i)
        return factors

    max_q = 0
    max_n = None
    for n in range(2,10001):
        toti = 1.0
        factors = factors_of(n)
        for i in range(2,n):
            coprime = True
            for factor in factors:
                if not i % factor:
                    coprime = False
                    break
            if coprime:
                toti += 1
        q = n/toti
        if q > max_q:
            max_q = q
            max_n = n
            print n, n/toti

    print(max_n, max_q)

#--------------------------------------------------------------------#

import timeit

times = []
for i in range(1):
    t = timeit.Timer('f{0}()'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0(): 
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
