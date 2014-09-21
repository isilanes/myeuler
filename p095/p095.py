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

    def next_m(N, propers):
        '''
        Return sum of proper divisors of N, potentially the next
        element in a amicable chain.
        '''
        
        return sum(propers[N])

    max_clen = 1
    max_chain = None
    for n in range(2,max+1):
        chain = [n]
        m = n
        while True:
            m = next_m(m, propers)
            if m == 1:
                break
            if m > max:
                break
            if m in chain:
                i = chain.index(m)
                clen = len(chain) - i
                if clen > max_clen:
                    max_clen = clen
                    max_chain = chain[i:]
                    print max_chain
                break
            chain.append(m)

def f1(max):
    print("--- f1 ---")

    # Find next-in-chain for all numbers up to max, using a sieve:
    propers = {}
    for i in range(1,max+1):
        p = i*2
        while p < max+1:
            try:
                propers[p].append(i)
            except:
                propers[p] = [i]
            p += i

    next_m = {}
    for k,v in propers.items():
        next_m[k] = sum(v)

    max_clen = 1
    max_chain = None
    for n in range(2,max+1):
        chain = [n]
        m = n
        while True:
            m = next_m[m]
            if m == 1:
                break
            if m > max:
                break
            if m in chain:
                i = chain.index(m)
                clen = len(chain) - i
                if clen > max_clen:
                    max_clen = clen
                    max_chain = chain[i:]
                    print max_chain
                break
            chain.append(m)

def f2(max):
    print("--- f2 ---")

    import math

    # Find next-in-chain for all numbers up to max, using a sieve.
    # Notice that next_m[N] overestimates the correct value by N,
    # as all divisors of N (including N itself) are included. To
    # compensate for it, we initialize next_m[N] to -N for every N.
    next_m = [ -x for x in range(max+1) ]
    for i in range(1,int(math.sqrt(max))+1):
        for j in range(i,max/i+1):
            p = i*j
            next_m[p] += i + j

    max_clen = 1
    max_chain = None
    for n in range(2,max+1):
        chain = [n]
        m = n
        while True:
            m = next_m[m]
            if m < n or m > max:
                break
            if m in chain:
                i = chain.index(m)
                clen = len(chain) - i
                if clen > max_clen:
                    max_clen = clen
                    max_chain = chain[i:]
                    print max_chain
                break
            chain.append(m)


#--------------------------------------------------------------------#

import timeit

times = []
for i in range(3):
    t = timeit.Timer('f{0}(1000*1000)'.format(i), "from __main__ import f{0}".format(i))
    times.append(t.timeit(number=1))

#
# f0: ~ 16 s (pypy)
# f1: ~ 10 s (pypy)
# f2: ~ 0.4 s (pypy)
#
print("\nTimes:\n")
for i in range(len(times)):
    print('t{0} = {1:.2f} ms'.format(i, times[i]*1000))
